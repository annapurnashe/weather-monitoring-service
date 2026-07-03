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

### 1. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
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
cd weather_project
venv\Scripts\activate  # Windows

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Access Swagger UI
```
http://localhost:8000/docs
```

---

## ⚙️ Running the Celery Worker

```bash
cd weather_project
venv\Scripts\activate  # Windows

celery -A app.tasks.weather_tasks worker --loglevel=info --pool=solo
```

---

## ⏰ Running the Scheduled Task

```bash
cd weather_project
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

### 2. List Cities (GET /cities)
```bash
curl http://localhost:8000/cities
```

### 3. Weather History (GET /cities/{city}/history)
```bash
curl http://localhost:8000/cities/Mumbai/history
```

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| POST | `/cities` | Add a new city |
| GET | `/cities` | List all cities |
| GET | `/cities/{city}/history` | Get weather history |

---

## 📁 Project Structure

```
weather_project/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── main.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── cities.py
│   ├── tasks/
│   │   ├── __init__.py
│   │   └── weather_tasks.py
│   └── utils/
│       ├── __init__.py
│       └── weather_api.py
├── venv/
├── requirements.txt
├── celery_worker.py
├── weather.db
└── README.md
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

**© 2026 Weather Monitoring Service**