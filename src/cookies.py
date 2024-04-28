
import os.path
import pickle


def save_cookies(driver):
    pickle.dump(driver.get_cookies() , open("saved_cookies/cookies.txt","wb"))

def load_cookies(driver):
    if os.path.exists("saved_cookies/cookies.txt") == False:
        print("No cookies found")
    else:
     cookies = pickle.load(open("saved_cookies/cookies.txt", "rb"))
     driver.execute_cdp_cmd('Network.enable', {})
     for cookie in cookies:
        if 'expiry' in cookie:
            cookie['expires'] = cookie['expiry']
            del cookie['expiry']
        driver.execute_cdp_cmd('Network.setCookie', cookie)
        driver.execute_cdp_cmd('Network.disable', {})





