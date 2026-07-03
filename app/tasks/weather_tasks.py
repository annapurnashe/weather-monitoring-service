from celery import Celery
from datetime import datetime
from app.config import Config
from app.database import SessionLocal
from app.models import MonitoredCity, WeatherHistory
from app.utils.weather_api import fetch_weather

celery_app = Celery(
    'weather_tasks',
    broker=Config.CELERY_BROKER_URL,
    backend=Config.CELERY_RESULT_BACKEND
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

@celery_app.task
def fetch_and_store_weather():
    db = SessionLocal()
    try:
        cities = db.query(MonitoredCity).all()
        for city in cities:
            weather_data = fetch_weather(city.latitude, city.longitude)
            if weather_data:
                weather_record = WeatherHistory(
                    city=city.city,
                    temperature=weather_data['temperature'],
                    wind_speed=weather_data['wind_speed'],
                    weather_code=weather_data['weather_code'],
                    fetched_at=datetime.utcnow()
                )
                db.add(weather_record)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
    finally:
        db.close()

celery_app.conf.beat_schedule = {
    'fetch-weather-every-minute': {
        'task': 'app.tasks.weather_tasks.fetch_and_store_weather',
        'schedule': Config.SCHEDULE_INTERVAL,
    },
}