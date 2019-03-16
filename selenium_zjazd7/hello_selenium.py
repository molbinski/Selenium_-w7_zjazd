# -*- coding: utf-8 -*-

#zaimportowanie bibliotek

from selenium import webdriver
import time


#stworz nowy sterownik
driver = webdriver.Chrome()
#maksymalizuj okno
driver.maximize_window()
driver.get("http://www.wsb.pl")
time.sleep(3)
# wylacz przegladarke
driver.quit()
