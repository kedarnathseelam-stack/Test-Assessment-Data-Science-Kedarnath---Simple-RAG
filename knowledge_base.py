import os

DOCS_FOLDER = "docs"

def load_documents():
    docs = []
    for file in os.listdir(DOCS_FOLDER):
        if file.endswith(".txt") or file.endswith(".md"):
            with open(os.path.join(DOCS_FOLDER, file), "r", encoding="utf-8") as f:
                docs.append({"filename": file, "content": f.read()})
    return docs
