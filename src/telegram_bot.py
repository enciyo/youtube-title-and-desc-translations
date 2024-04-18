import requests
from constants import CONST_TELEGRAM_TOKEN, CONST_TELEGRAM_CHAT_ID


def send_message(message):
    chat_ids = CONST_TELEGRAM_CHAT_ID.split(",")
    for chat_id in chat_ids:
        response = requests.get(f"https://api.telegram.org/bot{CONST_TELEGRAM_TOKEN}/sendMessage", {"chat_id": chat_id, "text": message})
        print(response.json())



def send_photo_file(file_path):
    with open(file_path, "rb") as f:
        chat_ids = CONST_TELEGRAM_CHAT_ID.split(",")
        for chat_id in chat_ids:
            response = requests.post(f"https://api.telegram.org/bot{CONST_TELEGRAM_TOKEN}/sendPhoto", {"chat_id": chat_id}, files={"photo": f})
            if response.status_code != 200:
                send_message(response.json())


