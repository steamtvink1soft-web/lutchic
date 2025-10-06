import http.server
import socketserver
import requests
import time
import subprocess

PORT = 8000  # порт, на котором будет запущен сервер
DIRECTORY = "C:\\Users\\лошарик\\PycharmProjects\\PythonProject4\\сайт 3"  # замените на реальный путь к папке
TOKEN = "7589790386:AAE0DukAgw0M3aOrarMVF4wezHy3gC_tERQ"   # Замените на токен вашего бота
AUTHORIZED_USER_ID = 7485606858    # Замените на ваш Telegram user ID
url = "Сервер запущен и работает. Доступ: http://192.168.0.11:8000/"


def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    try:
        requests.get(url, params=params)
    except Exception as e:
        send_message(f"Ошибка при отправке сообщения: {e}")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    with socketserver.TCPServer(("192.168.0.11", PORT), Handler) as httpd:
        print(f"Сервер запущен и работает. Доступ: http://192.168.0.11:{PORT}/")
        try:
            httpd.serve_forever()  # запуск и "бесконечная" работа сервера
        except KeyboardInterrupt:
            send_message("\nСервер остановлен.")