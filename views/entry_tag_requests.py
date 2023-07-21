import sqlite3
from models.entry_tag import EntryTag

def get_all_entry_tags():
    """
    Get all entry tags from the Entry_tags table.
    """
    with sqlite3.connect("your_database_file_name.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT id, tag_id, entry_id
            FROM Entry_tags
        """)

        entry_tags = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry_tag = EntryTag(row['id'], row['tag_id'], row['entry_id'])
            entry_tags.append(entry_tag.__dict__)

    return entry_tags

def get_single_entry_tag(id):
    """
    Get a single entry tag by ID.
    """
    with sqlite3.connect("your_database_file_name.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT id, tag_id, entry_id
            FROM Entry_tags
            WHERE id = ?
        """, (id,))

        row = db_cursor.fetchone()

        if row is not None:
            entry_tag = EntryTag(row['id'], row['tag_id'], row['entry_id'])
            return entry_tag.__dict__
        else:
            return None

def create_entry_tag(entry_tag):
    """
    Create a new entry tag and add it to the Entry_tags table.
    """
    with sqlite3.connect("your_database_file_name.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            INSERT INTO Entry_tags (tag_id, entry_id)
            VALUES (?, ?)
        """, (entry_tag['tag_id'], entry_tag['entry_id']))

        id = db_cursor.lastrowid

        entry_tag['id'] = id

    return entry_tag

def delete_entry_tag(id):
    """
    Delete an entry tag.
    """
    with sqlite3.connect("your_database_file_name.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            DELETE FROM Entry_tags
            WHERE id = ?
        """, (id,))

def update_entry_tag(id, new_entry_tag):
    """
    Update an entry tag.
    """
    with sqlite3.connect("your_database_file_name.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            UPDATE Entry_tags
            SET tag_id = ?, entry_id = ?
            WHERE id = ?
        """, (new_entry_tag['tag_id'], new_entry_tag['entry_id'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
