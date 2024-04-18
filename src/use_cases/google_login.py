from constants import CONST_EMAIL,CONST_PASSWORD,CONST_IS_ENABLE_OTP
from telegram_bot import send_photo_file
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
        sb.wait_for_element_visible(self.input_email)
        sb.type(self.input_email,CONST_EMAIL)
        sb.click(self.button_next)
        sb.type(self.input_password,CONST_PASSWORD)
        sb.click(self.button_next)
        if CONST_IS_ENABLE_OTP:
            sb.click(self.otp_input)
            sb.save_screenshot("otp_verification.png")
            send_photo_file("otp_verification.png")




