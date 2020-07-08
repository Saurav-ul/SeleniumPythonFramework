from selenium.webdriver.common.by import By

from PageObjects.TestCheckout import Tcheckout


class Homeshop:

    def __init__(self, driver):
        self.driver=driver

    shop = (By.LINK_TEXT,"Shop")
    def tshop(self):
         self.driver.find_element(*Homeshop.shop).click()
         checkout = Tcheckout(self.driver)
         return checkout

    name= (By.XPATH,"//div[@class='form-group']//input[@name='name']")
    email= (By.XPATH,"//input[@name='email']")
    submit= (By.XPATH,"//input[@type='submit']")

    def tname(self):
        return self.driver.find_element(*Homeshop.name)

    def temail(self):
        return self.driver.find_element(*Homeshop.email)

    def tsubmit(self):
        return self.driver.find_element(*Homeshop.submit)