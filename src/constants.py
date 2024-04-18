import os

CONST_YOUTUBE_STUDIO_URL = "https://studio.youtube.com/"
CONST_EMAIL = os.environ.get("YT_GOOGLE_EMAIL")
CONST_PASSWORD = os.environ.get("YT_GOOGLE_PASSWORD")
CONST_WAIT_GOOGLE_LOGIN_TIMEOUT = int(os.environ.get("YT_GOOGLE_LOGIN_TIMEOUT", 200))
CONST_WAIT_TRANSLATION_TIMEOUT = int(os.environ.get("YT_WAIT_TRANSLATION_TIMEOUT", 5))
CONST_IS_ENABLE_OTP = os.environ.get("YT_IS_ENABLE_OTP", False) == True






