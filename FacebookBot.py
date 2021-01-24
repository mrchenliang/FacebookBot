from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import random

from secrets import username, key

class FacebookBot():
    def __init__(self):
        self.driver = webdriver.Chrome("./chromedriver")
    
    def login(self):
        self.driver.get('https://facebook.com/login')
        sleep(1)
        email = self.driver.find_element_by_xpath('//*[@id="email"]')
        email.send_keys(username)
        password = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password.send_keys(key)
        login = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login.click()

    def event(self):
        self.driver.get('https://facebook.com/events/birthdays/')
        sleep(3)


    def post(self):
        WebDriverWait(self.driver,100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "._5rpu")))
        try:
            todays = self.driver.find_element_by_class_name('sjgh65i0')
            wish_forms = todays.find_elements_by_class_name('_5rpu')
            # todays = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]")
            # wish_forms = todays.find_elements_by_xpath("/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/form/div/div/div[1]/div/div/div[2]/div")
            names = todays.find_elements_by_class_name('cbu4d94t')
            for wish_form,name in zip(wish_forms,names[1:]):
                messages = [f'{name.text.split()[0]}, happy birthday!', f'happy birthday {name.text.split()[0]}!', f'happy birthday {name.text.split()[0]}!', 'happy birthday :D', 'Happy bday!!!']
                sendMessage = random.choice(messages)
                wish_form.send_keys(sendMessage)
                # Uncomment the next line to automatically send the wishes
                wish_form.send_keys(Keys.ENTER)
        except Exception as e:
                print(str(e))
        print("All Done!")

    def close(self):
        self.driver.close()

bot = FacebookBot()
bot.login()
bot.event()
bot.post()
bot.close()
