import sqlite3
from models.tag import Tag

def get_all_tags():
    """
    Get all tags from the Tags table.
    """
    with sqlite3.connect("dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT id, tag_name
            FROM Tags
        """)

        tags = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            tag = Tag(row['id'], row['tag_name'])
            tags.append(tag.__dict__)

    return tags

def get_single_tag(id):
    """
    Get a single tag by ID.
    """
    with sqlite3.connect("dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT id, tag_name
            FROM Tags
            WHERE id = ?
        """, (id,))

        row = db_cursor.fetchone()

        if row is not None:
            tag = Tag(row['id'], row['tag_name'])
            return tag.__dict__
        else:
            return None

def create_tag(tag):
    """
    Create a new tag and add it to the Tags table.
    """
    with sqlite3.connect("dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            INSERT INTO Tags (tag_name)
            VALUES (?)
        """, (tag['tag_name'],))

        id = db_cursor.lastrowid

        tag['id'] = id

    return tag

def delete_tag(id):
    """
    Delete a tag.
    """
    with sqlite3.connect("dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            DELETE FROM Tags
            WHERE id = ?
        """, (id,))

def update_tag(id, new_tag):
    """
    Update a tag.
    """
    with sqlite3.connect("dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            UPDATE Tags
            SET tag_name = ?
            WHERE id = ?
        """, (new_tag['tag_name'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
