import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Embedding model
EMBED_MODEL = "all-MiniLM-L6-v2"

# HF local small LLM - for simple summarization/QA
LLM_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

DB_PATH = "vectordb.sqlite"
CHUNK_SIZE = 300
CHUNK_OVERLAP = 50
TOP_K = 3
