from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

from secrets import username, key

class FacebookBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
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


    def post(self):

        counter = 1
        selected = self.driver.find_elements_by_xpath("//*[@id='birthdays_content']/div[1]/div[2]/ul/li[1]")
    # find_element_by_xpath('.//textarea[@aria-label="Write a birthday wish on his Timeline..."]')
        while(len(selected) > 0 ):
            html = selected[0].get_attribute('innerHTML')
            messageArea = selected[0].find_elements_by_xpath(".//textarea")
            fullName = html.split('aria-label="')[1].split('"')[0]
            name = fullName.split(" ")[0]

            message = [f'{name}, happy birthday!', f'happy birthday {name}!', f'happy birthday {name}!', 'happy birthday :D', 'Happy bday!!!']
            sendMessage = random.choice(message)

            if(len(messageArea) > 0):
                messageArea[0].send_keys(sendMessage)
                messageArea[0].send_keys(Keys.RETURN)
                sleep(0.75)
            else:
                pass
            counter += 1
            selected = self.driver.find_elements_by_xpath("//*[@id='birthdays_content']/div[1]/div[2]/ul/li["+str(counter)+"]")

        print("All Done!!")

    def close(self):
        self.driver.close()

bot = FacebookBot()
bot.login()
bot.event()
bot.post()
bot.close()
