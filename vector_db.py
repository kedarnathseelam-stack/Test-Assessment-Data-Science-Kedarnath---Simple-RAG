import os
from sqlite_vec import SqliteVec
from config import settings

os.makedirs("vector_db", exist_ok=True)

vec_db = SqliteVec(
    settings.DB_PATH,
    dim=settings.EMBED_DIM,
    table_name=settings.TABLE_NAME,
    auto_commit=True
)

def add_vector(item_id, vector, payload):
    vec_db.add_item(item_id=item_id, vector=vector, payload=payload)

def search_vectors(query_vec, top_k=3):
    return vec_db.search(query_vec, k=top_k)

def total_vectors():
    return len(vec_db)







