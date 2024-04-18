import requests
from constants import CONST_TELEGRAM_TOKEN, CONST_TELEGRAM_CHAT_ID


def send_photo_file(file_path: str):
    with open(file_path, "rb") as f:
        response = requests.put(f"https://api.telegram.org/bot{CONST_TELEGRAM_TOKEN}/sendPhoto", {"chat_id": CONST_TELEGRAM_CHAT_ID}, files={"photo": file_path})
        print(response.json())




