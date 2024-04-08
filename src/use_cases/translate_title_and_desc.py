from translate import translate_youtube_title_and_desc
from countries import get_country_code
from selenium.webdriver.common.keys import Keys


class TranslateTitleAndDesc:
    """
    A class that represents the use case for translating YouTube video title and description.

    Attributes:
        original_title_path (str): The CSS selector for the original title textarea element.
        original_desc_path (str): The CSS selector for the original description textarea element.
        translated_title_path (str): The CSS selector for the translated title textarea element.
        translated_desc_path (str): The CSS selector for the translated description textarea element.
        target_language_path (str): The CSS selector for the target language element.
        publish_button_path (str): The CSS selector for the publish button element.
        metadata_editor_path (str): The CSS selector for the metadata editor element.
    """

    original_title_path = "#original-title > div > textarea"
    original_desc_path = "#original-description > div > textarea"
    translated_title_path = "#translated-title > div > textarea"
    translated_desc_path = "#translated-description > div > textarea"
    target_language_path = "#language-name-row > div.metadata-editor-translated.style-scope.ytgn-metadata-editor > div"
    publish_button_path = "#publish-button > div"
    metadata_editor_path = "#metadata-editor"

    def invoke(self, sb):
        """
        Invokes the translation of YouTube video title and description.

        Args:
            sb (object): The object representing the Selenium browser.

        Returns:
            None
        """
        title = sb.find_element(self.original_title_path).get_attribute("value")
        description = sb.find_element(self.original_desc_path).get_attribute("value")
        video = translate_youtube_title_and_desc({
            "title": title,
            "description": description,
            "target_language": get_country_code(sb.find_element(self.target_language_path).text)
        })
        sb.type(self.translated_title_path, video["title"])
        sb.type(self.translated_desc_path, video["description"])
        editor = sb.find_element(self.metadata_editor_path)
        sb.click(self.publish_button_path)
        sb.execute_script("arguments[0].remove();",editor)





