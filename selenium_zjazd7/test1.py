# -*- coding: utf-8 -*-
# import bibliotek

from selenium import webdriver
import unittest

class WsbPLCheck(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #driver.get("http://www.wsb.pl")
        pass

    def tearDown(self):
        self.driver.quit()

    def test_wsb_pl(self):
        driver = self.driver
        driver.get("http://wsb.pl")

        #self.assertIn(u"Wyższe Szkoły Bankowe", driver.title)
        assert u"Wyższe Szkoły Bankowe" in driver.title

if __name__ == "__main__":
    unittest.main(verbosity=2)
