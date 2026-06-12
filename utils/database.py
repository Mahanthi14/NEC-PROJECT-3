import sqlite3
from pathlib import Path

DB_PATH = "database/healthcare.db"

def get_connection():
    Path("database").mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_default_users():
    conn = get_connection()
    cursor = conn.cursor()

    users = [
        ("patient", "patient123", "Patient"),
        ("doctor", "doctor123", "Doctor"),
        ("admin", "admin123", "Admin")
    ]

    for user in users:
        cursor.execute("""
        INSERT OR IGNORE INTO users (username, password, role)
        VALUES (?, ?, ?)
        """, user)

    conn.commit()
    conn.close()