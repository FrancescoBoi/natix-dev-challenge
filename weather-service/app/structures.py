"""
Moule providing custom structures
"""
from typing import TypedDict, List, Dict
from pydantic import BaseModel
from app.redis_structures import HourlyData

class APIHourlyData(HourlyData):
    """Structure representing Hourly data returned by APIs"""
    hour: int
    

class APIWeatherData(BaseModel):
    """
    Class representing a 
    """
    city: str
    result: List[APIHourlyData]