import sqlite3
from models.entry import Entry

def get_all_entries():
    """
    Get all entries from the Entries table.
    """
    with sqlite3.connect("dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT id, concept, entry, mood_id, date
            FROM Entries
        """)

        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'], row['mood_id'], row['date'])
            entries.append(entry.__dict__)

    return entries

def get_single_entry(id):
    """
    Get a single entry by ID.
    """
    with sqlite3.connect("dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT id, concept, entry, mood_id, date
            FROM Entries
            WHERE id = ?
        """, (id,))

        row = db_cursor.fetchone()

        if row is not None:
            entry = Entry(row['id'], row['concept'], row['entry'], row['mood_id'], row['date'])
            return entry.__dict__
        else:
            return None

def create_entry(entry):
    """
    Create a new entry and add it to the Entries table.
    """
    with sqlite3.connect("dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            INSERT INTO Entries (concept, entry, mood_id, date)
            VALUES (?, ?, ?, ?)
        """, (entry['concept'], entry['entry'], entry['mood_id'], entry['date']))

        id = db_cursor.lastrowid

        entry['id'] = id

    return entry

def delete_entry(id):
    """
    Delete an entry.
    """
    with sqlite3.connect("dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            DELETE FROM Entries
            WHERE id = ?
        """, (id,))

def update_entry(id, new_entry):
    """
    Update an entry.
    """
    with sqlite3.connect("dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            UPDATE Entries
            SET concept = ?, entry = ?, mood_id = ?, date = ?
            WHERE id = ?
        """, (new_entry['concept'], new_entry['entry'], new_entry['mood_id'], new_entry['date'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
