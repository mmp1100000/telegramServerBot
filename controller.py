from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

from main.utils import get_system_temperature

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

TOKEN = '1111140645:AAGIykn2MX6jCcs42xlAnKB8o12zNOiIS3I'

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


###
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


###
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


###
def get_temperature(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=get_system_temperature())


echo_handler = CommandHandler('temp', get_temperature)
dispatcher.add_handler(echo_handler)


updater.start_polling()
