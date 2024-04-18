from constants import CONST_EMAIL,CONST_PASSWORD,CONST_IS_ENABLE_OTP
from logger import take_screen_shot

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
    input_password = "input[type=password]"
    otp_input = "span:contains('Tap Yes on your phone or tablet')"

    def invoke(self, sb):
        """
        Invokes the Google login process by entering the email and clicking the 'Next' button.

        Args:
            sb: An instance of the SeleniumBase class.

        """
        take_screen_shot(sb)
        sb.wait_for_element_visible(self.input_email)
        take_screen_shot(sb)
        sb.click(self.button_next)
        take_screen_shot(sb)
        sb.type(self.input_password,CONST_PASSWORD)
        take_screen_shot(sb)
        sb.click(self.button_next)
        if CONST_IS_ENABLE_OTP:
            sb.click(self.otp_input)




