import sqlite3
from datetime import datetime

DATABASE = "crop_advisor.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            bot_response TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_chat(user_message, bot_response):
    conn = get_connection()

    conn.execute("""
        INSERT INTO chats (
            user_message,
            bot_response,
            created_at
        )
        VALUES (?, ?, ?)
    """, (
        user_message,
        bot_response,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_chat_history(limit=50):
    conn = get_connection()

    rows = conn.execute("""
        SELECT *
        FROM chats
        ORDER BY id DESC
        LIMIT ?
    """, (limit,)).fetchall()

    conn.close()

    history = []

    for row in rows:
        history.append({
            "id": row["id"],
            "user_message": row["user_message"],
            "bot_response": row["bot_response"],
            "created_at": row["created_at"]
        })

    return history


def clear_history():
    conn = get_connection()

    conn.execute("DELETE FROM chats")

    conn.commit()
    conn.close()

def create_users_table():
    conn = get_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def register_user(name, email, password):

    conn = get_connection()

    try:

        conn.execute("""
        INSERT INTO users(
            name,
            email,
            password
        )
        VALUES (?, ?, ?)
        """, (
            name,
            email,
            password
        ))

        conn.commit()

        return True

    except:

        return False

    finally:

        conn.close()


def login_user(email, password):

    conn = get_connection()

    user = conn.execute("""
    SELECT *
    FROM users
    WHERE email=?
    AND password=?
    """, (
        email,
        password
    )).fetchone()

    conn.close()

    return user