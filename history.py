from collections import defaultdict, deque

user_history = defaultdict(lambda: deque(maxlen=3))

def add_user_message(user_id, message):
    user_history[user_id].append(message)

def get_user_history(user_id):
    return list(user_history[user_id])
