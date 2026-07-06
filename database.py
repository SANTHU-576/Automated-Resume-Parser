import sqlite3

def create_database():
    conn = sqlite3.connect("resumes.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidates(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            skills TEXT,
            education TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_candidate(name, email, phone, skills, education):

    conn = sqlite3.connect("resumes.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO candidates(name, email, phone, skills, education)
        VALUES (?, ?, ?, ?, ?)
    """, (name, email, phone, skills, education))

    conn.commit()
    conn.close()