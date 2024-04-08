class AddLanguage:
    """
    Represents a use case for adding languages to a YouTube video.
    """

    attr_aria_disabled = "aria-disabled"
    list_path = "#paper-list [aria-disabled='false']"
    text_path = "ytcp-ve > tp-yt-paper-item-body > div > div > div > yt-formatted-string"

    def invoke(self, sb):
        """
        Invokes the use case to add a language to a YouTube video.

        Args:
            sb: An object representing the Selenium browser.

        Returns:
            A dictionary with the following keys:
            - "status": A boolean indicating the success status of the operation.
            - "lang": The language that was added, if the operation was successful.
        """
        if sb.is_element_visible(self.list_path):
            lang = sb.get_text(f"{self.list_path} > {self.text_path}")
            sb.scroll_to(self.list_path)
            sb.click(self.list_path)
            return {
                "status": True,
                "lang": lang
            }
        else:
            return {
                "status": False
            }
