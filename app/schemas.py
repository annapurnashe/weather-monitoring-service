from pydantic import BaseModel
from datetime import datetime

class CityCreate(BaseModel):
    city: str
    latitude: float
    longitude: float

class CityResponse(BaseModel):
    id: int
    city: str
    latitude: float
    longitude: float
    created_at: datetime
    
    class Config:
        from_attributes = True

class WeatherHistoryResponse(BaseModel):
    id: int
    city: str
    temperature: float
    wind_speed: float
    weather_code: int
    fetched_at: datetime
    
    class Config:
        from_attributes = True

















