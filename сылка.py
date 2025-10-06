import requests
import time

# Замените на реальные данные
BOT_TOKEN = "7589790386:AAE0DukAgw0M3aOrarMVF4wezHy3gC_tERQ"
CHAT_ID = "7485606858"
URL_TO_SEND = ("Сервер запущен и работает.\n"
               "Доступ: http://192.168.0.11:8000/\n")  # Ваша ссылка


def send_telegram_message():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        'chat_id': CHAT_ID,
        'text': f"Вот ваша ссылка:\n{URL_TO_SEND}",
        'disable_web_page_preview': False  # True - отключить превью сайта
    }
    time.sleep(1)
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print("Сообщение успешно отправлено!")
        else:
            print(f"Ошибка: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


send_telegram_message()