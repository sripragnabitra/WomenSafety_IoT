# 🚨 Women Safety IoT System

A real-time IoT-based safety monitoring system that detects emergency situations using sensor data, machine learning, and gesture-based triggers.

---

## 📌 Overview

This project simulates and implements a **women safety system** that:

- Monitors physiological + motion data
- Detects abnormal patterns using ML + rules
- Triggers emergency alerts
- Tracks live location
- Displays everything on a real-time dashboard

---

## ⚙️ Tech Stack

### Backend
- FastAPI (Python)
- SQLite (Database)
- ML Model (Scikit-learn)

### Frontend
- React.js
- Chart.js (Live graphs)
- Leaflet.js (Map visualization)

### IoT (Planned)
- ESP32
- Sensors (Heart Rate, Gyroscope, Microphone)
- GPS Module
- Buzzer/Vibration Motor

---

## 🧠 Features

### ✅ Implemented
- Sensor data ingestion (`/sensor`)
- Risk prediction (ML + gesture logic)
- Digital Twin (real-time state)
- Dashboard with history
- Live charts (heart rate, temperature, motion)
- Live map tracking (lat/lon)
- Emergency detection logic:
  - 1 spike → Normal
  - 2 spikes → Emergency

---

### 🚧 Upcoming (with hardware)
- ESP32 integration
- Real sensor data
- GPS-based live tracking
- Physical alert system (vibration/buzzer)

---

## 📂 Project Structure
iot/
├── backend/
│ ├── main.py
│ ├── api/routes.py
│ ├── ml/
│ ├── database/safety.db
│ └── utils/helpers.py
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ │ ├── Dashboard.jsx
│ │ │ ├── DigitalTwin.jsx
│ │ │ ├── Charts.jsx
│ │ │ └── MapView.jsx
│ │ └── services/api.js
│
├── esp32/ (future)
└── README.md


---

## 🚀 How to Run

## 1. Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Backend runs at:
http://127.0.0.1:8000

## 2. Frontend

```bash
cd frontend
npm install
npm start

Frontend runs at:
http://localhost:3000

3. Test API (Swagger)

Go to: http://127.0.0.1:8000/docs

Use:
/sensor → send data
/dashboard → view history
/digital_twin → latest state

🔁 Data Flow

Sensor/Simulator sends data → /sensor

Backend:
Stores in DB
Predicts risk

Frontend:
Fetches /digital_twin (live)
Fetches /dashboard (history)
UI updates automatically

🚨 Risk Detection Logic

Based on:
Heart rate
Temperature
Motion
Gesture spikes

Rules:
Normal → safe state
Emergency → triggers alert + vibration

📊 Digital Twin

A real-time virtual representation of the user’s state:
Heart Rate
Temperature
Motion
Risk Level
Location

Auto-refresh every few seconds.

🗺️ Live Tracking

Displays user location on map
Updates dynamically using backend data

📌 Future Scope

Mobile app integration
SMS / call alerts
Cloud deployment
AI-based anomaly detection
Wearable device integration

📜 License

This project is for academic and research purposes.