import telegram
from telegram.ext import CommandHandler, Updater

TOKEN = '5911375448:AAENINTNh3IdYEDKrXqtY5xKWIfXxiVAwBU'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот, который отнимает от числа 20% и умножает на 0.5. Попробуй ввести число после команды /calculate")

def calculate(update, context):
    number = float(context.args[0])
    result = (number - (number * 0.2)) * 0.5
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Результат: {result}")

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('calculate', calculate))

updater.start_polling()
