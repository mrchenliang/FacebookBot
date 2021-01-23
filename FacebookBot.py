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
                message = [f'{name}, happy birthday!', f'happy birthday {name}!', f'happy birthday {name}!', 'happy birthday :D', 'Happy bday!!!']
                sendMessage = random.choice(message)
                msg = sendMessage
                wish_form.send_keys(msg)
                # Uncomment the next line to automatically send the wishes
                ## wish_form.send_keys(Keys.ENTER)
        except Exception as e:
                print(str(e))

    #     counter = 1
    #     selected = self.driver.find_elements_by_class("j83agx80 pybr56ya rz4wbd8a sj5x9vvc a8nywdso")
    # # find_element_by_xpath('.//textarea[@aria-label="Write a birthday wish on his Timeline..."]')
    #     while(len(selected) > 0 ):
    #         html = selected[0].get_attribute('innerHTML')
    #         messageArea = selected[0].find_elements_by_xpath(".//textarea")
    #         fullName = html.split('aria-label="')[1].split('"')[0]
    #         name = fullName.split(" ")[0]

    #         message = [f'{name}, happy birthday!', f'happy birthday {name}!', f'happy birthday {name}!', 'happy birthday :D', 'Happy bday!!!']
    #         sendMessage = random.choice(message)

    #         if(len(messageArea) > 0):
    #             messageArea[0].send_keys(sendMessage)
    #             messageArea[0].send_keys(Keys.RETURN)
    #             sleep(0.75)
    #         else:
    #             pass
    #         counter += 1
    #         selected = self.driver.find_elements_by_xpath("//*[@id='birthdays_content']/div[1]/div[2]/ul/li["+str(counter)+"]")

        print("All Done!")

    def close(self):
        self.driver.close()

bot = FacebookBot()
bot.login()
bot.event()
bot.post()
# bot.close()
