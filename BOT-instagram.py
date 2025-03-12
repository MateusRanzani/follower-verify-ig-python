from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
from secret import pw, user

class IGBot: 
    def __init__(self):
        self.driver = webdriver.Chrome()

    def loggin(self):
        driver = self.driver
        url = 'https://instagram.com/'
        driver.get(url)

        time.sleep(5)

        #User
        user_name = driver.find_element("name", "username")
        user_name.click()

        time.sleep(2)
        user_name.send_keys(user)

        #Key
        user_password = driver.find_element("name", "password")
        user_password.click()

        time.sleep(3)
        user_password.send_keys(pw)

        #Loggin
        user_password.send_keys(Keys.ENTER)
        time.sleep(6)

        #2FA

task = IGBot()
task.loggin()