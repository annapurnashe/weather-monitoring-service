from fastapi import FastAPI
from app.routes import cities
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Weather Monitoring Service")
app.include_router(cities.router)

@app.get("/")
def root():
    return {"message": "Weather Monitoring Service", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy"}


