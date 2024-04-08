from constants import CONST_EMAIL

class GoogleLogin:
    """
    A class representing the Google login functionality.

    Attributes:
        input_email (str): CSS selector for the email input field.
        button_next (str): CSS selector for the 'Next' button.

    Methods:
        invoke(sb, email): Invokes the Google login process by entering the email and clicking the 'Next' button.
    """
    input_email = "input[type=email]"
    button_next = "button[type=button] > span:contains(Next)"

    def invoke(self, sb):
        """
        Invokes the Google login process by entering the email and clicking the 'Next' button.

        Args:
            sb: An instance of the SeleniumBase class.
        """
        sb.wait_for_element_visible(self.input_email)
        sb.type(self.input_email, CONST_EMAIL)
        sb.click(self.button_next)
