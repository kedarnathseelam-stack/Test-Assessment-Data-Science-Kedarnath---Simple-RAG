
from sentence_transformers import SentenceTransformer
from vector_db import search_vectors
from cache import load_cache, save_cache
from config import settings

embedder = SentenceTransformer(settings.EMBED_MODEL)

def retrieve(query, top_k=3):
    cached = load_cache("retrieval_" + query)
    if cached:
        return cached["context"], cached["sources"]

    query_vec = embedder.encode(query)
    results = search_vectors(query_vec, top_k)

    context = "\n\n".join([r.payload["text"] for r in results])
    sources = [r.payload["source"] for r in results]

    save_cache("retrieval_" + query, {"context": context, "sources": sources})

    return context, sources







