from retrieval import retrieve
from generation import generate_answer

def rag(query):
    retrieved = retrieve(query)
    answer = generate_answer(query, retrieved)
    return answer, retrieved
