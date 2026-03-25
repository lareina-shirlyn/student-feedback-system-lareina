"""
Student Feedback System - Database Module (SQLite)
"""

import sqlite3
import os

# database file path
DB_PATH = os.path.join(os.path.dirname(__file__), "feedback.db")


def get_connection():
    """Create database connection"""
    return sqlite3.connect(DB_PATH)


def init_db():
    """Create feedback table if not exists"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            message TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_feedback(name, message):
    """Insert feedback"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO feedback (name, message) VALUES (?, ?)",
        (name, message)
    )

    conn.commit()
    conn.close()


def get_feedbacks():
    """Get all feedback"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM feedback")
    data = cursor.fetchall()

    conn.close()
    return data
