import sqlite3

def create_table():
    conn = sqlite3.connect("leetcode_tracker.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS problems(
        id INTEGER PRIMARY KEY,
        title TEXT,
        difficulty TEXT,
        category TEXT,
        date_solved TEXT,
        notes TEXT
    )
    """)

    conn.commit()
    conn.close()

def get_all_problems_db():
    conn = sqlite3.connect("leetcode_tracker.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM problems")

    rows = cursor.fetchall()

    conn.close()

    return rows

create_table()

rows = get_all_problems_db()

print(rows)

def add_problem_db(problem):

    conn = sqlite3.connect("leetcode_tracker.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO problems
    (title, difficulty, category, date_solved, notes)
    VALUES (?, ?, ?, ?, ?)
    """, (
        problem["title"],
        problem["difficulty"],
        problem["category"],
        problem["date_solved"],
        problem["notes"]
    ))

    conn.commit()
    conn.close()