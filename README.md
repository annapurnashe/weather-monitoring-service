# 🌤️ Weather Monitoring Service

A FastAPI-based weather monitoring service that automatically fetches weather data for configured cities every minute using Celery and Redis.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.10.11** | Programming Language |
| **FastAPI** | Web Framework for REST APIs |
| **Celery** | Task Queue for Background Tasks |
| **Redis** | Message Broker for Celery |
| **SQLite** | Lightweight Database |
| **SQLAlchemy** | ORM for Database Operations |
| **Uvicorn** | ASGI Server |
| **Pydantic** | Data Validation |

---

## 📁 Project Setup

### 1. Clone or Download Project
```bash
git clone https://github.com/annapurnashe/weather-monitoring-service.git
cd weather-monitoring-service
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 📦 Dependency Installation

### requirements.txt
```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
celery==5.3.4
redis==5.0.1
requests==2.31.0
pydantic==2.5.0
python-dotenv==1.0.0
```

---

## 🗄️ Database Schema

**Table: monitored_cities**
```sql
CREATE TABLE monitored_cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city VARCHAR(100) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

**Table: weather_history**
```sql
CREATE TABLE weather_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city VARCHAR(100) NOT NULL,
    temperature FLOAT NOT NULL,
    wind_speed FLOAT NOT NULL,
    weather_code INTEGER NOT NULL,
    fetched_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🔴 Redis Setup

### Windows
1. Download: https://github.com/microsoftarchive/redis/releases
2. Install `Redis-x64-3.0.504.msi`
3. Start Redis:
```bash
redis-server
```

### Verify Redis
```bash
redis-cli ping
# Output: PONG
```

---

## 🚀 Running the FastAPI Application

```bash
cd weather-monitoring-service
venv\Scripts\activate  # Windows

uvicorn app.main:app --reload --host localhost --port 8000
```

### Access Swagger UI
```
http://localhost:8000/docs
```

---

## ⚙️ Running the Celery Worker

```bash
cd weather-monitoring-service
venv\Scripts\activate  # Windows

celery -A app.tasks.weather_tasks worker --loglevel=info --pool=solo
```

---

## ⏰ Running the Scheduled Task

```bash
cd weather-monitoring-service
venv\Scripts\activate  # Windows

celery -A app.tasks.weather_tasks beat --loglevel=info
```

---

## 🧪 Testing the APIs

### 1. Add City (POST /cities)
```bash
curl -X POST http://localhost:8000/cities \
  -H "Content-Type: application/json" \
  -d '{"city": "Mumbai", "latitude": 19.0760, "longitude": 72.8777}'
```

**Response:**
```json
{
  "id": 1,
  "city": "Mumbai",
  "latitude": 19.076,
  "longitude": 72.8777,
  "created_at": "2026-07-03T10:30:45"
}
```

### 2. List Cities (GET /cities)
```bash
curl http://localhost:8000/cities
```

**Response:**
```json
[
  {
    "id": 1,
    "city": "Mumbai",
    "latitude": 19.076,
    "longitude": 72.8777,
    "created_at": "2026-07-03T10:30:45"
  }
]
```

### 3. Weather History (GET /cities/{city}/history)
```bash
curl http://localhost:8000/cities/Mumbai/history
```

**Response:**
```json
[
  {
    "id": 1,
    "city": "Mumbai",
    "temperature": 29.5,
    "wind_speed": 12.3,
    "weather_code": 3,
    "fetched_at": "2026-07-03T10:31:00"
  }
]
```

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| POST | `/cities` | Add a new city |
| GET | `/cities` | List all cities |
| GET | `/cities/{city}/history` | Get weather history for a city |

---

## 📁 Project Structure

```
weather-monitoring-service/
│
├── app/
│   ├── __init__.py
│   ├── config.py          # Configuration settings
│   ├── database.py        # Database connection
│   ├── models.py          # Database models
│   ├── schemas.py         # Pydantic schemas
│   ├── main.py            # FastAPI application
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   └── cities.py      # City API routes
│   │
│   ├── tasks/
│   │   ├── __init__.py
│   │   └── weather_tasks.py  # Celery tasks
│   │
│   └── utils/
│       ├── __init__.py
│       └── weather_api.py    # Weather API calls
│
├── venv/                    # Virtual environment
├── requirements.txt         # Dependencies
├── celery_worker.py         # Celery worker entry point
├── weather.db              # SQLite database
└── README.md               # Documentation
```

---

## ✅ Features

- ✅ Add cities with latitude/longitude
- ✅ List all monitored cities
- ✅ View weather history for specific cities
- ✅ Automatic weather data collection every 1 minute
- ✅ Clean modular architecture
- ✅ RESTful API design
- ✅ Swagger UI documentation

---

## 📝 Notes

- Weather data is fetched from Open-Meteo API (No API key required)
- Weather codes: 0=Clear, 1-3=Partly cloudy, 45-48=Fog, 51-67=Drizzle/Rain, 71-77=Snow, 80-99=Thunderstorm
- Celery Beat runs the weather fetch task every 1 minute
- SQLite database is created automatically on first run


**© 2026 Weather Monitoring Service**
