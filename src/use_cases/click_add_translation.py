class ClickAddTranslations:
     """
     A class representing the use case of clicking the 'Add Translations' button.

     Attributes:
          button (str): The CSS selector of the 'Add Translations' button.

     Methods:
          invoke(sb): Invokes the use case by checking if the button is visible and clicking it if so.

     """

     button = "#add-translations-button"

     def invoke(self, sb):
          """
          Invokes the use case by checking if the button is visible and clicking it if so.

          Args:
               sb: An instance of the SeleniumBase class.

          Returns:
               bool: True if the button is visible, False otherwise.

          """
          isElementVisible = sb.is_element_visible(self.button)
          if isElementVisible:
               sb.click(self.button)
          return isElementVisible

