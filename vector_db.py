import sqlite3
from sqlite_vec import Vec
import numpy as np
from config import DB_PATH

class VectorDB:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.enable_load_extension(True)
        Vec.load(self.conn)
        self.init_table()

    def init_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS chunks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                doc_name TEXT,
                chunk TEXT,
                embedding BLOB
            );
        """)
        self.conn.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS vec_index USING vec0(
                id INTEGER PRIMARY KEY,
                embedding FLOAT[384]
            );
        """)

    def insert(self, doc_name, chunk, embedding):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO chunks (doc_name, chunk, embedding) VALUES (?, ?, ?)",
            (doc_name, chunk, embedding.astype(np.float32).tobytes())
        )
        chunk_id = cursor.lastrowid
        self.conn.execute(
            "INSERT INTO vec_index(id, embedding) VALUES (?, ?)",
            (chunk_id, embedding.tolist())
        )
        self.conn.commit()

    def search(self, query_emb, top_k=3):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id, distance FROM vec_index
            WHERE embedding MATCH ?
            ORDER BY distance LIMIT ?;
        """, (query_emb.tolist(), top_k))

        results = []
        for chunk_id, dist in cursor.fetchall():
            chunk_row = self.conn.execute(
                "SELECT doc_name, chunk FROM chunks WHERE id=?", (chunk_id,)
            ).fetchone()
            results.append({"doc": chunk_row[0], "chunk": chunk_row[1], "distance": dist})
        return results
