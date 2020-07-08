import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.TestCheckout import Tcheckout
from PageObjects.TestShop import Homeshop
from PageObjects.Testpurchase import Purchase
from Utilities.BaseClass import TestBaseClass


class TestE2E(TestBaseClass):

    def test_endtoendtestcase(self):

        log= self.getlogger()
        homeshop= Homeshop(self.driver)
        checkout=homeshop.tshop()
        log.info("Moved to checkout page")

        ctitle=checkout.tcardtitle()
        for i in ctitle:
            pnames=i.text
            print(pnames)
            if pnames=="Blackberry":
                checkout.tcardlist().click()
        checkout.tcardcheck1().click()
        testpurchase=checkout.tcardcheck2()
        log.info("Moved to purchase page")

        testpurchase.tcountryname().send_keys("ind")
        self.tlinkpresence("India")
        #time.sleep(10)
        testpurchase.tcountryselection().click()
        testpurchase.tbutton1().click()
        testpurchase.tbutton2().click()
        a=testpurchase.tbutton3().text
        print(a)
        assert "Success" in a
        #driver.get_screenshot_as_file("screen.png")

