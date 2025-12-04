
from embedd import build_vector_db
from bot import run_bot

if __name__ == "__main__":
    build_vector_db(force=False)
    run_bot()







