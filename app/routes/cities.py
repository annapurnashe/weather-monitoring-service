from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import MonitoredCity, WeatherHistory
from app.schemas import CityCreate, CityResponse, WeatherHistoryResponse

router = APIRouter()

@router.post("/cities", response_model=CityResponse, status_code=201)
def add_city(city: CityCreate, db: Session = Depends(get_db)):
    existing = db.query(MonitoredCity).filter(MonitoredCity.city == city.city).first()
    if existing:
        raise HTTPException(status_code=400, detail="City already exists")
    
    db_city = MonitoredCity(
        city=city.city,
        latitude=city.latitude,
        longitude=city.longitude
    )
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

@router.get("/cities", response_model=List[CityResponse])
def list_cities(db: Session = Depends(get_db)):
    return db.query(MonitoredCity).all()

@router.get("/cities/{city}/history", response_model=List[WeatherHistoryResponse])
def get_city_history(city: str, db: Session = Depends(get_db)):
    history = db.query(WeatherHistory).filter(
        WeatherHistory.city == city
    ).order_by(WeatherHistory.fetched_at.desc()).all()
    
    if not history:
        raise HTTPException(status_code=404, detail="No history found")
    return history