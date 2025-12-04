from embed import Embedder
from vector_db import VectorDB
from cache import EmbedCache
from config import TOP_K

embedder = Embedder()
db = VectorDB()
cache = EmbedCache()

def retrieve(query):
    # Avoid re-embedding if already cached
    cached = cache.get(query)
    if cached is not None:
        query_emb = cached
    else:
        query_emb = embedder.embed(query)
        cache.set(query, query_emb)

    results = db.search(query_emb, top_k=TOP_K)
    return results
