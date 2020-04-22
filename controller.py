from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

from main.utils import get_system_temperature

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

TOKEN = '1111140645:AAGIykn2MX6jCcs42xlAnKB8o12zNOiIS3I'

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
job_queue = updater.job_queue


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
    temp = get_system_temperature()
    context.bot.send_message(chat_id=update.effective_chat.id, text=temp)


echo_handler = CommandHandler('temp', get_temperature)
dispatcher.add_handler(echo_handler)


def job_temperature(context: CallbackContext):
    temp = get_system_temperature()
    temp_value = float(temp[temp.index('=') + 1:temp.index('\'')])
    if temp_value > 55.0:
        context.bot.send_message(chat_id='@rpialerts',
                                 text=temp)


job_minute = job_queue.run_repeating(job_temperature, interval=10, first=20 )

updater.start_polling()
