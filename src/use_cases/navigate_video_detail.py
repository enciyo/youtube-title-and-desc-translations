from selenium.webdriver.common.by import By

class NavigateToVideoDetail:
    """
    A class that represents the use case of navigating to a video detail page.

    Methods:
        __create_cell_xpath: Creates the XPath for a video cell based on the index.
        invoke: Invokes the use case by clicking on a video cell.
    """

    languages_count = "#languages-count"

    def __create_cell_xpath(self, index):
        """
        Creates the XPath for a video cell based on the index.

        Args:
            index (int): The index of the video cell.

        Returns:
            str: The XPath for the video cell.
        """
        return f"#table-content > ytgn-video-row:nth-child({index}) > #row-container > div.tablecell-video.floating-column.last-floating-column.cell-body.style-scope.ytgn-video-row.style-scope.ytgn-video-row > ytcp-video-list-cell-video > #video-thumbnail > #thumbnail-anchor"

    def invoke(self, sb, index):
        """
        Invokes the use case by clicking on a video cell.

        Args:
            sb: The object representing the Selenium browser.
            index (int): The index of the video cell.
        """
        path = self.__create_cell_xpath(index + 1)
        count = path.find_element(By.CSS_SELECTOR, self.languages_count).text()
        if count != "233":
            sb.wait_for_element_visible(path)
            sb.click(path)
