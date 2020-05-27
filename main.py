import requests
import telegram
import os

print(telegram.__version__)

# TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
# CHAT_ID = os.environ.get('CHAT_ID')
#
#
# def send():
#     bot = telegram.Bot(token=TELEGRAM_TOKEN)
#     return bot.send_message(chat_id=CHAT_ID, text='Я живой!!')
#
#
# if __name__ == '__main__':
#     send()
