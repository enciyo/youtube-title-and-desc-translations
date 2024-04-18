import os
import time
from constants import CONST_WORKSPACE

count = 0
def take_screen_shot(sb):
    global count
    count += 1
    sb.save_screenshot(f"screenshot{count}.png")
    os.system(f"mv screenshot{count}.png {CONST_WORKSPACE}")



def append_log_file(message):
    with open(f"{CONST_WORKSPACE}/log.txt", "a") as file:
        file.write(f"{time.ctime()} - {message}\n")
        file.close()





