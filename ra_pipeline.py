from sentence_transformers import SentenceTransformer
from retrieval import retrieve
from generation import generate_answer
from collections import defaultdict, deque

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_answer(query, context_chunks):
    context = "\n\n".join([c["chunk"] for c in context_chunks])
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    return f"Based on the documents:\n{context[:400]}...\n\nThis answers your query."

def rag(query):
    retrieved = retrieve(query)
    answer = generate_answer(query, retrieved)
    return answer, retrieved

user_history = defaultdict(lambda: deque(maxlen=3))

def add_user_message(user_id, message):
    user_history[user_id].append(message)

def get_user_history(user_id):
    return list(user_history[user_id])
