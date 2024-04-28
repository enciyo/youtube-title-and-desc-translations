from easygoogletranslate import EasyGoogleTranslate
from truncate import truncate
from constants import CONST_WAIT_TRANSLATION_TIMEOUT

def safe_translate(egt,text, target_language):
    try:
        return egt.translate(text)
    except Exception as e:
        print(f"Error translating text: {text} to {target_language}")
        print(e)
        return text


def translate_youtube_title_and_desc(video):
    target_language = video['target_language']
    egt = EasyGoogleTranslate(
            source_language='en',
            target_language=target_language,
            timeout=CONST_WAIT_TRANSLATION_TIMEOUT,
        )
    title = video['title']
    description = video['description']
    translated_title = safe_translate(egt,title,target_language)
    translated_description = safe_translate(egt,description,target_language)
    return {
        "title": truncate(translated_title,100),
        "description": truncate(translated_description,5000)
    }


