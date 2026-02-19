import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "safety.db")

def save_to_db(data, risk):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO data (heart_rate, temperature, motion, risk, lat, lon)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["heart_rate"],
        data["temperature"],
        data["motion"],
        risk,
        data.get("lat"),
        data.get("lon")
    ))

    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    SELECT heart_rate, temperature, motion, risk 
    FROM data ORDER BY id DESC LIMIT 20
    """)
    
    rows = cur.fetchall()
    conn.close()

    return [
        {
            "heart_rate": r[0],
            "temperature": r[1],
            "motion": r[2],
            "risk": r[3]
        }
        for r in rows
    ]

def get_latest_state():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT heart_rate, temperature, motion, risk, lat, lon FROM data ORDER BY rowid DESC LIMIT 1")
    row = cur.fetchone()

    conn.close()

    if row is None:
        return {
            "heart_rate": 0,
            "temperature": 0,
            "motion": 0,
            "risk": "SAFE",
            "lat": 0,
            "lon": 0
        }

    return {
        "heart_rate": row[0],
        "temperature": row[1],
        "motion": row[2],
        "risk": row[3],
        "lat": row[4],
        "lon": row[5]
    }