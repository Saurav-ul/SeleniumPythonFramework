from selenium.webdriver.common.by import By


class Purchase:

    def __init__(self,driver):
        self.driver=driver

    countryname= (By.ID,"country")
    countryselection=(By.LINK_TEXT,"India")
    button1=(By.CSS_SELECTOR,"div[class*='checkbox-primary']")
    button2=(By.CSS_SELECTOR,"input[class*='btn-success']")
    button3=(By.CSS_SELECTOR,"div[class*='alert-success']")

    def tcountryname(self):
        return self.driver.find_element(*Purchase.countryname)
    def tcountryselection(self):
        return self.driver.find_element(*Purchase.countryselection)
    def tbutton1(self):
        return self.driver.find_element(*Purchase.button1)
    def tbutton2(self):
        return self.driver.find_element(*Purchase.button2)
    def tbutton3(self):
        return self.driver.find_element(*Purchase.button3)
