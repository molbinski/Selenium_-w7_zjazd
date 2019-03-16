# -*- coding: utf-8 -*-
# import bibliotek

from selenium import webdriver
import unittest
import time

class WizzAirRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl#/")

    def tearDown(self):
        self.driver.quit()

    def test_wrong_email(self):
        driver = self.driver
        #1. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
        zaloguj_sie_button = driver.find_element_by_xpath("//button[@data-test='navigation-menu-signin']")
        zaloguj_sie_button.click()
        #2. Wybierz rejestracja
        rejestracja_button = driver.find_element_by_xpath("//button[text()='Rejestracja']")
        rejestracja_button.click()
        #3. Wprowadź imię
        imie_atrybut = driver.find_element_by_name("firstName")
        imie_atrybut.send_keys("Darek")
        #4. Wprowadź nazwisko
        nazwisko_atrybut = driver.find_element_by_xpath("//input[@placeholder='Nazwisko']")
        nazwisko_atrybut.send_keys(u"Otwórz")
        time.sleep(5)
        #5. Wybierz płeć
        
        #6. Wprowadź nr tel
        #7. Wprowadź błędny adres email - brak znaku @
        #8. Wprowadź hasło
        #9. Wybierz kraj
        #10. Akceptuj politykę prywatności
        #11. Kliknij przycisk ZAREJESTRUJ SIĘ"


        #1. Przycisk "zarejestruj się" jest nieaktywny
        #2. Użytkownik dostaje informację, że wprowadzony e-mail jest niepoprawny
        #assert u"" in

if __name__ == "__main__":
    unittest.main(verbosity=2)
