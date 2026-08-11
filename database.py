import sqlite3
from pathlib import Path

DB_NAME = Path(__file__).with_name("hotel_booking.db")

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            room_id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_number TEXT NOT NULL UNIQUE,
            room_type TEXT NOT NULL,
            price REAL NOT NULL,
            status TEXT NOT NULL DEFAULT 'Available'
        )
    """)

    conn.commit()
    conn.close()

def register_user(username, password, email):
    conn = get_connection()
    try:
        conn.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (username, password, email)
        )
        conn.commit()
        return True, "Registration successful."
    except sqlite3.IntegrityError as e:
        if "username" in str(e).lower():
            return False, "Username is already taken."
        if "email" in str(e).lower():
            return False, "Email is already registered."
        return False, "Registration failed."
    finally:
        conn.close()

def authenticate_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, username, email FROM users WHERE username = ? AND password = ?",
        (username, password)
    )
    user = cursor.fetchone()
    conn.close()
    return user

def seed_rooms():
    conn = get_connection()
    cursor = conn.cursor()
    count = cursor.execute("SELECT COUNT(*) FROM rooms").fetchone()[0]

    if count == 0:
        rooms = [
            ("101", "Single", 35.00, "Available"),
            ("102", "Double", 55.00, "Available"),
            ("201", "Deluxe", 80.00, "Available"),
            ("202", "Family", 100.00, "Available"),
            ("301", "Suite", 150.00, "Available"),
        ]
        cursor.executemany(
            "INSERT INTO rooms (room_number, room_type, price, status) VALUES (?, ?, ?, ?)",
            rooms
        )
        conn.commit()
    conn.close()
