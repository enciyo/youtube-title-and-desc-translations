class GetVideos:
    """
    A class that represents the use case for getting videos.

    Attributes:
        list (str): The CSS selector for the video list.

    Methods:
        invoke(sb): Invokes the use case by waiting for the video list element to be visible and then finding all the video elements.

    """

    list = "#table-content > ytgn-video-row"

    def invoke(self, sb):
        """
        Invokes the use case by waiting for the video list element to be visible and then finding all the video elements.

        Args:
            sb: The instance of the SeleniumBase object.

        Returns:
            list: A list of video elements.

        """
        sb.wait_for_element_visible(self.list)
        return sb.find_elements(self.list)


