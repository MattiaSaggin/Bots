from time import sleep
from selenium import webdriver
import TelegramSentinel

class PS5Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.amazon.')
        sleep(50)

    def checkAndBuyPS5(self):
        self.driver.get('URLo del SIUMMMM')
        sleep(1)
        try:
            buyNow = self.driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')                     #aggiungi al carrello
            buyNow.click()
            if buyNow:
                TelegramSentinel.alarm()
            self.driver.close()


        except Exception as e:
            print(e)
            sleep(1.5)
            self.checkAndBuyPS5()
bot = PS5Bot()
bot.login()
bot.checkAndBuyPS5()
