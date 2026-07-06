from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.database import Base

class MonitoredCity(Base):
    __tablename__ = 'monitored_cities'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(100), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

class WeatherHistory(Base):
    __tablename__ = 'weather_history'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(100), nullable=False)
    temperature = Column(Float, nullable=False)
    wind_speed = Column(Float, nullable=False)
    weather_code = Column(Integer, nullable=False)
    fetched_at = Column(DateTime, server_default=func.now())





