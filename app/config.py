class Config:
    DATABASE_URL = 'sqlite:///weather.db'
    REDIS_URL = 'redis://localhost:6379/0'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    WEATHER_API_URL = 'https://api.open-meteo.com/v1/forecast'
    SCHEDULE_INTERVAL = 60