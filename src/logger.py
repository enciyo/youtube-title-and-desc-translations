import os
import time
from constants import CONST_WORKSPACE

count = 0
def take_screen_shot(sb):
    global count
    count += 1
    a = sb.save_screenshot(f"screenshot{count}.png")
    print(str(a))
    os.system(f"mv screenshot{count}.png output")



def append_log_file(message):
    print( f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")





