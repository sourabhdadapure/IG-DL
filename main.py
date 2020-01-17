from selenium import webdriver
from time import sleep

class InstagramBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys('un')
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys('pw')
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(5)
        self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")').click()
        sleep(5)

InstagramBot('un', 'pw')