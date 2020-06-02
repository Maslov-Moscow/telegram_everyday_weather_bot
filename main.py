import requests
import telegram
import os
# from dotenv import load_dotenv

from datetime import datetime

# load_dotenv()  # delete on deploy

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
WEATHER_TOKEN = os.environ.get('WEATHER_TOKEN')


def send(message):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)  # , request=proxy)
    return bot.send_message(chat_id=CHAT_ID, text=message)


def parse_weather():
    params = {
        "appid": WEATHER_TOKEN,
        'lon': 37.62,
        'lat': 55.75,
        "exclude": "current,minutely,hourly",
        'lang': 'ru',
        'units': 'metric'}

    response = requests.get(f"http://api.openweathermap.org/data/2.5/onecall", params=params)

    morning = response.json()['daily'][1]['temp']['morn']
    evening = response.json()['daily'][1]['temp']['eve']
    night = response.json()['daily'][1]['temp']['night']
    description = response.json()['daily'][1]['weather'][0]['description']

    date = int(response.json()['daily'][1]['dt'])
    value = datetime.datetime.fromtimestamp(date)
    date_r = value.strftime('%d-%m-%Y')

    message = f'{date_r}\nУтром:{int(morning)}С°\nВечером:{int(evening)}С°\nНочью:{int(night)}С°\nПогода:{description}'
    return message


def timer():
    # response = requests.get('http://worldtimeapi.org/api/timezone/Europe/Moscow')
    # utctime = response.json()['utc_datetime']
    utctime = datetime.now()
    print(f'Бот запущен\n{utctime}')

    pass


if __name__ == '__main__':
    send(parse_weather())
    send(timer())