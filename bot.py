from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from rag_pipeline import rag
from history import add_user_message, get_user_history
from config import TELEGRAM_BOT_TOKEN
from generation import generate_answer

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = """
Commands:
/ask <query> — Ask any question with RAG
/summarize — Summarize last conversation
/help — Show this help
"""
    await update.message.reply_text(msg)

async def ask_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    query = " ".join(context.args)
    add_user_message(user_id, query)

    answer, snippets = rag(query)

    snippet_text = "\n\n".join([f"[{s['doc']}]: {s['chunk'][:150]}..." for s in snippets])

    await update.message.reply_text(f"{answer}\n\nSources:\n{snippet_text}")

async def summarize_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    history = "\n".join(get_user_history(user_id))

    summary = generate_answer("Summarize this:", [{"chunk": history}])

    await update.message.reply_text(summary)

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("ask", ask_cmd))
    app.add_handler(CommandHandler("summarize", summarize_cmd))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
