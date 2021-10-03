from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import json

def options():

    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    opt.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic": 2, 
        "profile.default_content_setting_values.media_stream_camera": 2,
        "profile.default_content_setting_values.geolocation": 2, 
        "profile.default_content_setting_values.notifications": 2 })
        
    return opt

def login(data, driver):

    login_button = driver.find_elements_by_class_name("glue-header__link")[3]
    login_button.click()
    
    email_in = driver.find_elements_by_class_name("whsOnd")[0]
    email_in.send_keys(data["email"])
    email_in.send_keys(Keys.RETURN)
    time.sleep(7)

    pass_in = driver.find_elements_by_class_name("whsOnd")[0]
    pass_in.send_keys(data["password"])
    pass_in.send_keys(Keys.RETURN)
    time.sleep(7)

def join(data, driver):

    meetCode_button = driver.find_elements_by_class_name("VfPpkd-fmcmS-wGMbrd")[0]
    meetCode_button.send_keys(data["code"])
    meetCode_button.send_keys(Keys.RETURN)
    time.sleep(7)

    dismiss_button = driver.find_elements_by_class_name("U26fgb")[4]
    dismiss_button.click()
    time.sleep(15)

    join_button = driver.find_elements_by_class_name("uArJ5e")[0]
    join_button.click()
    time.sleep(7)

def chat(driver):
    
    chat_button = driver.find_elements_by_class_name("r6xAKc")[2]
    chat_button.click()
    time.sleep(7)

    lastMessage = "null"
    lastDatetime = -1
    alive = True

    while alive:

        newMessages = getMessage(driver)
        size = len(newMessages)
        
        msg = buildMessage(newMessages[max(0,size-10):],lastMessage,lastDatetime)

        if msg != "NULL":
            sendMessage(driver, msg)
            lastDatetime = newMessages[-1]["minute"]
            lastMessage = msg

        time.sleep(30)

def buildMessage(buffer, lastMessage, lastDatetime):

    if len(buffer) == 0:
        return "NULL"
    
    difference = buffer[-1]["minute"] - buffer[0]["minute"]

    if difference > 5: # 5 min diff
        return "NULL"
    
    if lastDatetime != -1 and buffer[-1]["minute"] - lastDatetime <= 5:
        return "NULL"

    dict = {}

    for m in buffer:
        if m["text"] == "":
            continue
        
        key = m["text"].capitalize()
        if key in dict.keys():
            x = dict[key]
            dict[key] = x + 1
        else:
            dict[key] = 1

    best = ("NULL",4)
    
    for pair in dict.items():
        if pair[1] > best[1]:
            best = pair
    
    if best[0] == "NULL":
        return "NULL"
    
    if lastMessage == best[0] and buffer[-1]["minute"] - lastDatetime <= 5:
        return "NULL"

    return best[0]


def sendMessage(driver, message):
    
    textArea = driver.find_element_by_name("chatTextInput")
    textArea.send_keys(message)
    textArea.send_keys(Keys.RETURN)

def getMessage(driver):

    try:
        messageRaw = driver.find_elements_by_class_name("GDhqjd")
    except:
        messageRaw = []

    buffer = []

    for mRaw in messageRaw:
        name = mRaw.get_attribute("data-sender-name")
        minute = parseInt(mRaw.get_attribute("data-formatted-timestamp"))
        
        texts = mRaw.find_elements_by_class_name("oIy2qc")

        for t in texts:
            text = t.get_attribute("data-message-text")
            message = {
                "name": name,
                "minute": minute,
                "text": text
            }

            buffer.append(message)
    
    return buffer

def parseInt(temp):

    if temp == '':
        print("time vazio")
        return 0

    hour = int(temp.split(':')[0])
    minute = int(temp.split(':')[1])

    temp = hour*60 + minute

    return temp

def main():

    link = "https://meet.google.com/"

    try:
        f = open("data.json","r")
    except:
        print("o arquivo data.json nao foi encontrado.")
        print("Por favor, visite github.com/kinhosz/Diana")
        exit(0)

    data = json.loads(f.read())
    f.close()

    try:
        driver = webdriver.Chrome(options=options(),executable_path="./driver/chromedriver.exe")
    except:
        print("Nao foi encontrado o webdriver")
        print("Por favor, visite github.com/kinhosz")
        exit(0)

    driver.get(link)

    login(data, driver)

    join(data, driver)

    chat(driver)

    driver.close()

if __name__ == "__main__":
    main()