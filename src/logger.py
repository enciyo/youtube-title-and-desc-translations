import os
import time
from constants import CONST_WORKSPACE

count = 0
def take_screen_shot(sb):
    global count
    count += 1
    sb.driver.save_screenshot(f"screenshot{count}.png")
    os.system(f"mv screenshot.png {CONST_WORKSPACE}")


def append_log_file(message):
    with open(f"{CONST_WORKSPACE}/log.txt","a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

