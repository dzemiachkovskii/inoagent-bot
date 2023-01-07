import os
from telebot import TeleBot
from message import inoagent_message

print(os.environ['HOME'])
BOT_TOKEN = os.getenv('INO_BOT_TOKEN')
bot = TeleBot(BOT_TOKEN)


@bot.message_handler()
def main(m):
    if m.text.lower() == "иноагент" and hasattr(m.reply_to_message, "message_id"):
        inoagent = m.reply_to_message
        bot.delete_message(m.chat.id, m.message_id)
        bot.reply_to(inoagent, inoagent_message)


bot.infinity_polling()
