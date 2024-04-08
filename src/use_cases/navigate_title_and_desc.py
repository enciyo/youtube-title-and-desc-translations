from selenium.webdriver.common.by import By

class NavigateTitleAndDescription:
    """
    This class represents a use case for navigating the title and description of a YouTube video translation.
    """

    hover_path = "div.tablecell-metadata.cell-body.style-scope.ytgn-video-translation-row.style-scope.ytgn-video-translation-row > ytgn-video-translation-cell-metadata > div"
    add_button = "ytgn-video-translation-cell-metadata > div > ytgn-video-translation-hover-cell > #cell-container > #hover-items-container > ytcp-icon-button[aria-label=Add]"

    def __create_row_path(self, language):
        """
        Creates a JavaScript code snippet to find the row element for a given language.

        Args:
            language (str): The language to search for.

        Returns:
            str: The JavaScript code snippet.
        """
        return f"""
              const rows = document.querySelectorAll("div#table-list ytgn-video-translation-row div#row-container");
              const targetRow = Array.from(rows).find(row => {{
              const languageDiv = row.querySelector("div.language-text");
                    return languageDiv && languageDiv.textContent.trim() === "{language}";
                    }});
              return targetRow;
  """


    def invoke(self,sb,language):
        row = self.__create_row_path(language)
        parent = sb.execute_script(row)
        parent.find_element(By.CSS_SELECTOR,self.hover_path).click()
        parent.find_element(By.CSS_SELECTOR,self.add_button).click()

