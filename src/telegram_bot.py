import requests
from constants import CONST_TELEGRAM_TOKEN, CONST_TELEGRAM_CHAT_ID


def send_photo_file(file_path: str):
    with open(file_path, "rb") as photo:
        response = requests.post(f"https://api.telegram.org/bot{CONST_TELEGRAM_TOKEN}/sendPhoto", data={"chat_id": CONST_TELEGRAM_CHAT_ID}, files={"photo": photo})
    return response.json()
