# app/db/metadata.py
import sqlite3
import os

DB_PATH = "document_metadata.db"

# Initialize database on module import
if not os.path.exists(DB_PATH):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                document_id TEXT PRIMARY KEY,
                filename TEXT,
                num_chunks INTEGER
            );
        """)

def save_metadata(document_id: str, filename: str, chunks: list):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO documents (document_id, filename, num_chunks) VALUES (?, ?, ?)",
            (document_id, filename, len(chunks))
        )
        conn.commit()

def get_all_metadata():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("SELECT document_id, filename, num_chunks FROM documents")
        return [
            {"document_id": row[0], "filename": row[1], "num_chunks": row[2]}
            for row in cursor.fetchall()
        ]
