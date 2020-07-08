from selenium.webdriver.common.by import By

from PageObjects.Testpurchase import Purchase


class Tcheckout:

    def __init__(self,driver):
        self.driver=driver

    cardtitle= (By.CSS_SELECTOR,".card-title")
    cardlist= (By.XPATH,"//app-card-list/app-card[4]/div/div[2]/button")
    check1= (By.CSS_SELECTOR,"a[class*='btn']")
    check2= (By.CSS_SELECTOR,"button[class*='btn-success']")

    def tcardtitle(self):
        return self.driver.find_elements(*Tcheckout.cardtitle)
    def tcardlist(self):
        return self.driver.find_element(*Tcheckout.cardlist)
    def tcardcheck1(self):
        return self.driver.find_element(*Tcheckout.check1)
    def tcardcheck2(self):
        self.driver.find_element(*Tcheckout.check2).click()
        testpurchase = Purchase(self.driver)
        return testpurchase