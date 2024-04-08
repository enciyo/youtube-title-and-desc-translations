from constants import CONST_WAIT_GOOGLE_LOGIN_TIMEOUT

class NavigateToSubtitle:
    """
    A class that represents the use case of navigating to the subtitle menu.

    Attributes:
        menu_subtitle (str): The CSS selector for the subtitle menu.

    Methods:
        invoke(sb): Invokes the use case by waiting for the subtitle menu to be clickable and then clicking it.
    """
    menu_subtitle = "#main-menu > li:nth-child(13)"

    def invoke(self, sb):
        """
        Invokes the use case by waiting for the subtitle menu to be clickable and then clicking it.

        Args:
            sb (object): The object representing the web browser or automation tool.

        Returns:
            None
        """
        sb.wait_for_element_clickable(self.menu_subtitle, timeout=CONST_WAIT_GOOGLE_LOGIN_TIMEOUT)
        sb.click(self.menu_subtitle)



