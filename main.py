import logging
import os

import telebot
from flask import Flask
from telebot import TeleBot, types

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

bot.message_handler(content_types=['text'])


def main(m):
    bot.send_message(m.chat.id, m)
