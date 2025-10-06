import requests
import subprocess
from config import comad_bot

url = "Сервер запущен и работает. Доступ: http://192.168.0.11:8000/"
TOKEN = "7589790386:AAE0DukAgw0M3aOrarMVF4wezHy3gC_tERQ"   # Замените на токен вашего бота
AUTHORIZED_USER_ID = 7485606858    # Замените на ваш Telegram user ID
PROCESS = None
import time

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    try:
        requests.get(url, params=params)
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")

def start_code(chat_id):
    global PROCESS
    if PROCESS is None:
        try:
            PROCESS = subprocess.Popen(["python", "лол.py"])
            PROCESS = subprocess.Popen(["python", "сылка.py"])
            send_message(chat_id, "Cайт запущен.")
        except Exception as e:
            send_message(chat_id, f"Ошибка при запуске: {e}")
    else:
        send_message(chat_id, "Код уже запущен.")

def stop_code(chat_id):
    global PROCESS
    if PROCESS is not None:
        try:
            PROCESS.terminate()
            PROCESS.wait(timeout=5)
            PROCESS = None
            send_message(chat_id, "Cайт остановлен.")
        except Exception as e:
            send_message(chat_id, f"Ошибка при остановке: {e}")
    else:
        send_message(chat_id, "Cайт не запущен.")

def restart_code(chat_id):
    global PROCESS
    try:
        if PROCESS is not None:
            PROCESS.terminate()
            PROCESS.wait(timeout=5)
        PROCESS = subprocess.Popen(["python", "лол.py"])
        PROCESS = subprocess.Popen(["python", "сылка.py"])
        send_message(chat_id, "Cайт перезапущен.")
    except Exception as e:
        send_message(chat_id, f"Ошибка при перезапуске: {e}")

def process_message(update):
    message = update.get('message')
    if not message:
        return

    chat_id = message['chat']['id']
    user_id = message['from']['id']
    text = message.get('text', '')

    if user_id != AUTHORIZED_USER_ID:
        send_message(chat_id, "У вас нет прав на управление ботом.")
        return

    if text.startswith('/'):
        cmd = text.split()[0].lower()

        if cmd == '/starte':
            start_code(chat_id)
            return

        if cmd == '/stop':
            stop_code(chat_id)
            return

        if cmd == '/restart':
            restart_code(chat_id)
            return

        send_message(chat_id, "")

def main():
    last_update_id = None
    print("Бот запущен, ожидание команд...")
    while True:
        url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
        if last_update_id:
            url += f"?offset={last_update_id + 1}"
        try:
            r = requests.get(url, timeout=1)
            r.raise_for_status()
            result = r.json()
            for update in result.get('result', []):
                process_message(update)
                last_update_id = update['update_id']
        except Exception as e:
            print(f"Ошибка получения обновлений: {e}")

if __name__ == '__main__':
    send_message(AUTHORIZED_USER_ID, comad_bot)
    main()