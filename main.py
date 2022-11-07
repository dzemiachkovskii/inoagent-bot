import logging
import os

import telebot
from flask import Flask, request
from telebot import TeleBot, types

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler()
def main(m):
    x = bot.reply_to_message.message.id
    bot.send_message(m.chat.id, x)
    bot.delete_message(m.chat.id, m.message_id)


@server.route(f'/{BOT_TOKEN}', methods=['POST'])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


APP_URL = os.environ.get('APP_URL')
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
