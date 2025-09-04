from typing import List, Dict
from pydantic import BaseModel

class Date(BaseModel):
    """
    Class to represent last update of the redis update with hour granularity
    """
    year: int
    month: int
    day: int
    hour: int

class HourlyData(BaseModel):
    """
    Structure representing a single hour weather data
    """
    temperature: str
    condition: str

class RedisEntry(BaseModel):
    """
    Class representing a 
    """
    last_update: Date
    data: List[Dict[int, HourlyData]]