import pytest

from PageObjects.TestShop import Homeshop
from Testdata.Homepagetestdata import Homepagetestdata
from Utilities.BaseClass import TestBaseClass


class Testformfill(TestBaseClass):

    def test_formfillhome(self,getdata):
        log = self.getlogger()
        fill= Homeshop(self.driver)
        fill.tname().send_keys(getdata["Name"])
        fill.temail().send_keys(getdata["Email"])
        fill.tsubmit().click()
        log.debug("Successfully submitted")

    @pytest.fixture(params=Homepagetestdata.gettestdata("Testcase2"))
    def getdata(self,request):
        return request.param