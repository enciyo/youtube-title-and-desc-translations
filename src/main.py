from seleniumbase import SB
from constants import *
from cookies import load_cookies, save_cookies
from use_cases.google_login import GoogleLogin
from use_cases.navigate_subtitle import NavigateToSubtitle
from use_cases.get_videos import GetVideos
from use_cases.navigate_video_detail import NavigateToVideoDetail
from use_cases.click_add_translation import ClickAddTranslations
from use_cases.add_languages import AddLanguage
from use_cases.navigate_title_and_desc import NavigateTitleAndDescription
from use_cases.translate_title_and_desc import TranslateTitleAndDesc
import time
from telegram_bot import send_message,send_photo_file


def main():
    """
    This script automates the process of adding translations to YouTube video titles and descriptions.
    It uses SeleniumBase library for web automation and performs the following steps:
    1. Opens the YouTube Studio URL.
    2. Performs Google login.
    3. Navigates to the subtitle section.
    4. Retrieves the list of videos.
    5. For each video, navigates to the video detail page.
    6. Clicks on the "Add translations" button.
    7. Adds the specified language to the video title and description.
    8. Translates the title and description using the Google Translate API.
    9. Waits for 5 seconds before completing the script.

    Note: This script assumes that the necessary use case classes and constants are imported correctly.
    """
    chromium_args = ",".join([
        "--disable-extensions",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--headless",
    ])

    with SB(uc=True,headless2=True,chromium_arg=chromium_args) as sb:
        load_cookies(sb.driver)
        sb.refresh()
        try:
            # Open the YouTube Studio URL
            sb.open(CONST_YOUTUBE_STUDIO_URL)

            if "accounts.google.com" in sb.get_current_url():
                # Perform Google login
                GoogleLogin().invoke(sb)
            # Navigate to the subtitle section
            NavigateToSubtitle().invoke(sb)
            # Get the list of videos
            videoCount = len(GetVideos().invoke(sb))
            for index in range(videoCount):
                # Navigate to the video detail page
                NavigateToVideoDetail().invoke(sb,index)
                # Click on the "Add translations" button for the video
                while ClickAddTranslations().invoke(sb):
                    # Add the language to the video title and description
                    add_action = AddLanguage().invoke(sb)
                    if add_action["status"] == True:
                        # Navigate to the title and description section
                        NavigateTitleAndDescription().invoke(sb,add_action["lang"])
                        # Translate the title and description
                        TranslateTitleAndDesc().invoke(sb)
                    else:
                        # No more languages to add
                        print(f"No more languages to add for this video ({index}). Moving to the next video.")
                        break
                print(f"Completed adding translations for video {index}")
                send_message(f"Completed adding translations for video {index}")
                sb.go_back()

            save_cookies(sb.driver)
            sb.wait(5)
        except Exception as e:
            save_cookies(sb.driver)
            with open("error.log", "w") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {str(e)}\n")
            sb.save_screenshot("error.png")
            send_photo_file("error.png")
            send_message(f"An error occurred: {str(e)}")



if __name__ == "__main__":
    main()

