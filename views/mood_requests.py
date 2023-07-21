import sqlite3
from models.mood import Mood

def get_all_moods():
    """
    Get all moods from the Moods table.
    """
    with sqlite3.connect("dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT id, label
            FROM Moods
        """)

        moods = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            mood = Mood(row['id'], row['label'])
            moods.append(mood.__dict__)

    return moods

def get_single_mood(id):
    """
    Get a single mood by ID.
    """
    with sqlite3.connect("dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT id, label
            FROM Moods
            WHERE id = ?
        """, (id,))

        row = db_cursor.fetchone()

        if row is not None:
            mood = Mood(row['id'], row['label'])
            return mood.__dict__
        else:
            return None

def create_mood(mood):
    """
    Create a new mood and add it to the Moods table.
    """
    with sqlite3.connect("dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            INSERT INTO Moods (label)
            VALUES (?)
        """, (mood['label'],))

        id = db_cursor.lastrowid

        mood['id'] = id

    return mood

def delete_mood(id):
    """
    Delete a mood.
    """
    with sqlite3.connect("dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            DELETE FROM Moods
            WHERE id = ?
        """, (id,))

def update_mood(id, new_mood):
    """
    Update a mood.
    """
    with sqlite3.connect("dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            UPDATE Moods
            SET label = ?
            WHERE id = ?
        """, (new_mood['label'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
