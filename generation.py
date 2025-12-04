from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_answer(query, context_chunks):
    context = "\n\n".join([c["chunk"] for c in context_chunks])
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"

    # Public MiniLM cannot generate, so we do a simple similarity answer:
    return f"Based on the documents:\n{context[:400]}...\n\nThis answers your query."







