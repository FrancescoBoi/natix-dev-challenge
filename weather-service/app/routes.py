"""
Module implementing endpoints and some utilities
"""
from datetime import datetime
import json
from typing import Optional
from flask import request, jsonify
from app import app, redis
from app.structures import HourlyData, RedisEntry, Date, APIWeatherData
from app.externals import get_weather_data

def get_last_update(last_updated: Optional[Date]=None) -> bool:
    """
    Function compares the passed datetime to the current
    and return the old object if year, month, day and hour are the same, the new one if not
    or if the input is none.

    Args:
        last_updated (dict): datetime of the last updated entry in Redis

    Returns:
        bool: true if the redis entry needs to be updated, i.e., the last entry
              does not contain the new hour(s)
    """
    current_date = datetime.now()
    current_date: Date = Date(year=current_date.year, month=current_date.month,
                      day=current_date.day, hour=current_date.hour)
    new_update_date = last_updated
    if last_updated is None:
        new_update_date = current_date
    elif current_date.year>last_updated.year or current_date.month>last_updated.month or \
            current_date.day>last_updated.day or current_date.hour>last_updated.hour:
        new_update_date = current_date
    return new_update_date


@app.route('/weather')
def weather():
    """
    Decorator for "/weather" endpoing
    Returns:
    """
    try:
        city: str = request.args.get('city').lower().capitalize()
    except:
        return jsonify({"result": []})
    redis_entry: RedisEntry = redis.get(city)
    last_weather_data = {}
    if not redis_entry:
        # no entry means it's the first insertion for that city
        dict_date: Date = Date.model_validate(get_last_update())
        new_entry: RedisEntry = RedisEntry.model_validate({"last_update": dict_date, "data": list()})
        # ASSUMPTION: a dictionary is returned directly
        # ASSUMPTION: external api returns same data for past hours
        #get data from external call
        weather_data: APIWeatherData = APIWeatherData.model_validate(get_weather_data(city))
        for hour_weather in weather_data.result:
            hour_weather_json = hour_weather.model_dump()
            new_entry.data.append({int( hour_weather_json.pop("hour")) : hour_weather_json})
        redis.set(city, new_entry.model_dump_json())
        last_weather_data = weather_data
    else:
        redis_data: RedisEntry = RedisEntry.model_validate(json.loads(redis.get(city)))
        last_update: Date = Date.model_validate(redis_data.last_update)
        new_update_date: Date = Date.model_validate(get_last_update(last_update))
        if last_update == new_update_date:
            # convert data from redis represention to API
            weather_data: APIWeatherData = APIWeatherData.model_validate(
                {
                    "city": city,
                    "result": [{"hour": list(element.keys())[0], **list(element.values())[0].model_dump()} 
                        for element in redis_data.data
                    ]
                }
            )
            last_weather_data = weather_data
        else:
            # call external service
            weather_data: APIWeatherData = APIWeatherData.model_validate(get_weather_data(city))
            last_hours_inserted: int = len(redis_data.data)-1
            for new_hourly_data in weather_data.result[last_hours_inserted+1:]:
                hour_weather_json = new_hourly_data.model_dump()
                hourly_data = {hour_weather_json.pop("hour") : hour_weather_json}
                redis_data.data.append(hourly_data)
            redis_data.last_update = new_update_date
            redis.set(city, redis_data.model_dump_json())
            last_weather_data = weather_data
    return jsonify(last_weather_data.model_dump())
