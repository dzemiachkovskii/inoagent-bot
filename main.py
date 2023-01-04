import os
from telebot import TeleBot, types
from flask import Flask, request
from message import inoagent_message

BOT_TOKEN = os.environ.get('INO_BOT_TOKEN')
bot = TeleBot(BOT_TOKEN)
server = Flask(__name__)
WEBHOOK_LISTEN = "0.0.0.0"
WEBHOOK_HOST = "45.141.102.1"
WEBHOOK_PORT = 8443
WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % BOT_TOKEN


@bot.message_handler()
def main(m):
    if m.text.lower() == "иноагент" and hasattr(m.reply_to_message, "message_id"):
        inoagent = m.reply_to_message
        bot.delete_message(m.chat.id, m.message_id)
        bot.reply_to(inoagent, inoagent_message)


@server.route(f'/{BOT_TOKEN}', methods=['POST'])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH)
    server.run(host=WEBHOOK_LISTEN, port=WEBHOOK_PORT)
