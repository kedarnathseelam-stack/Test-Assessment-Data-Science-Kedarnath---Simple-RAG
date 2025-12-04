# RAG Telegram Bot

This is a lightweight Retrieval Augmented Generation chatbot that runs fully locally and communicates through a Telegram bot.  
It uses a small embedding model, a local sqlite vec vector database, and a mini-generation component based on a local Hugging Face model.

# Features

- Receive user messages via Telegram commands  
- `/ask <query>` → Perform a full RAG pipeline  
- `/summarize` → Summarize last 3 user queries  
- `/help` → Help menu  
- Mini-RAG built on a small knowledge base  
- Local embeddings using **all-MiniLM-L6-v2**  
- Local sqlite-vec vector search  
- No cloud APIs required  
- Embedding cache (no re-embedding repeated queries)  
- Source snippets returned to user  

---

# Models & APIs Used

### **1. Embedding Model**
sentence-transformers/all-MiniLM-L6-v2

Used for:
- Document chunk embeddings  
- Query embeddings  

### **2. Local LLM (Small Text Generator)**
sentence-transformers/all-MiniLM-L6-v2

Used for:
- Lightweight summarization  
- Context-aware answer formatting  
> It is used here as a lightweight local model to produce heuristic answers and summaries.  
> This helps keep the project **lightweight and local with no API costs**.

### **3. sqlite-vec**
Used for:
- Storing embeddings inside a local SQLite DB  
- Performing top-k vector similarity search  

### **APIs Used**
**None.**
- No OpenAI API  
- No external inference APIs  

All inference is **local**.

# Installation

### 1. Clone the repository
git clone [https://github.com/<your-repo>/<project>.git](https://github.com/kedarnathseelam-stack/Test-Assessment-Data-Science-Kedarnath---Simple-RAG)
cd <project>
2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate         
3. Install dependencies
pip install -r requirements.txt
4. Add the Telegram token
Create a .env file:
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_TOKEN
Build the Vector Database (Run Once)
python build_db.py
This script will:
Load documents from /docs
Chunk them
Embed them
Insert them into the sqlite vec database

Run the Bot Locally
The main entry file is bot.py
