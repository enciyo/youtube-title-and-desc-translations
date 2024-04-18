import os
import time
from constants import CONST_WORKSPACE

count = 0
def take_screen_shot(sb):
    global count
    count += 1
    sb.driver.save_screenshot(f"screenshot{count}.png")
    os.system(f"mv screenshot{count}.png {CONST_WORKSPACE}")


def append_log_file(message):
    path = f"{CONST_WORKSPACE}/log.txt"
    if not os.path.exists(path):
        with open(path,"w") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")
    else:
        with open(path,"a") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")



