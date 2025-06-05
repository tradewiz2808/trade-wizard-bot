import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

def respond_to_message(text: str) -> str:
    text = text.lower()
    if "analyze aapl" in text:
        return "🔍 AAPL Break & Retest\nEntry: $192.45\nSL: $191.70\nTP: $195.00\nConfidence: High"
    elif "news tsla" in text:
        return "📰 TSLA Sentiment: Bearish\n- Tesla delays production\n- Stock dropped 3%"
    elif "journal" in text:
        return "📓 Journal: 5 Trades | 4 Wins ✅ | 1 Loss ❌ | 80% Win Rate"
    elif "coach" in text:
        return "🧠 Coach Tip:\nLook for clean breakout + pullback + rejection wick.\nEnter on confirmation."
    else:
        return "🤖 I didn’t get that. Try:\n'analyze AAPL'\n'news TSLA'\n'journal'\n'coach'"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = respond_to_message(user_message)
    await update.message.reply_text(response)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to Trade Wizard!\nType something like:\n'analyze AAPL'\n'news TSLA'\n'journal'\n'coach'")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Trade Wizard is running...")
    app.run_polling()

if __name__ == "__main__":
    main()