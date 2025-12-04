import hashlib

class EmbedCache:
    def __init__(self):
        self.cache = {}

    def key(self, text):
        return hashlib.md5(text.encode()).hexdigest()

    def get(self, text):
        return self.cache.get(self.key(text))

    def set(self, text, emb):
        self.cache[self.key(text)] = emb
