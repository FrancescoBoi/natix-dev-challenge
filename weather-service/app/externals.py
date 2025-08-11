"""
Module to simulate external calls.
"""
from datetime import datetime, timedelta
import random
from app.structures import APIWeatherData

def get_weather_data(city: str):
    """Function to simulate external API returning weather ata

    Args:
        city (str): the city for which weather data should be returned

    Returns:
        _type_: weather data
    """
    # after 1hr the counter must be reset
    MAX_TIME_DELTA = timedelta(hours=1)
    date = datetime.now()
    
    if len(get_weather_data.calls) == 0:
        pass # date will be added at the end
    elif (date - get_weather_data.calls[0])>MAX_TIME_DELTA:
        # remove old calls
        i = 0
        for i, call in enumerate(get_weather_data.calls):
            if date-call<MAX_TIME_DELTA:
                break
        get_weather_data.calls = get_weather_data.calls[i:]
    elif len(get_weather_data.calls)>=100:
        return {}
    weather_type = {0:"Cloudy", 1: "Clear", 2: "Rainy", 3: "Foggy"}
    result: APIWeatherData  = dict()
    result["city"] = city
    result["result"] = list()
    base_temp = random.randrange(-20,35)
    temp = base_temp
    for i in range(date.hour+1):
        temp = temp + random.randrange(-3,3)
        result["result"].append({ "hour": i, "temperature": str(temp)+"°C", 
                                 "condition": weather_type[random.randrange(0,len(weather_type))] })
    get_weather_data.calls.append(date)
    return result

get_weather_data.calls = list()
