from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from voice_engine import make_voice

# SET THESE
TOKEN = "8194243995:AAHAnA9sseQ6nuKIdRDEiabENruxutkWHuk"
GROUP_ID = -1002859720960   # Replace with your group ID
OWNER_ID = 6892997376        # Your Telegram ID

bot = Bot(token=TOKEN)
app = Flask(__name__)
dp = Dispatcher(bot, None, workers=0, use_context=True)

def handle_message(update, context):
    user_id = update.message.from_user.id
    text = update.message.text

    # Convert text to speech
    file_path = make_voice(text)

    if user_id == OWNER_ID:
        # Send voice back to owner's DM
        bot.send_voice(chat_id=user_id, voice=open(file_path, 'rb'))
    else:
        # Send voice to group
        bot.send_voice(chat_id=GROUP_ID, voice=open(file_path, 'rb'),
                       caption=f"👤 @{update.message.from_user.username or 'unknown'}: {text}")

dp.add_handler(MessageHandler(Filters.text & Filters.private, handle_message))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dp.process_update(update)
    return "ok"

@app.route("/")
def index():
    return "Gnex TTS Bot is Running!"

if __name__ == "__main__":
    app.run()