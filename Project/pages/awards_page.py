import time
import pytest
from .locators import *
from selenium import webdriver
from .base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class AwardsPage(BasePage):
    def guest_look_awards(self):
        n = 0
        for i in range(1, 50):
            try:
                look_awards1 = self.browser.find_element(By.CSS_SELECTOR, f".view-content div:nth-child({i}) .row .large-10 a").text
                look_awards = self.browser.find_element(By.CSS_SELECTOR, \
                                                         f".view-content div:nth-child({i}) .row .large-10 a").click()
                look_awards_check = self.browser.find_element(*AwardsPageLocators.AWARDS_TITLE).text
                assert look_awards1 == look_awards_check, f"guest_look_awards error {look_awards1} != {look_awards_check}"
                action = ActionChains(self.browser)
                open_submenu = self.browser.find_element(*BasePageLocators.SUBMENU_COMPANY)
                action.move_to_element(open_submenu).perform()
                section = self.browser.find_element(By.CSS_SELECTOR,
                                                    ".first.expanded.has-dropdown .dropdown li:nth-child(4) a").click()
                n += 1
            except NoSuchElementException:
                print(f"Test Find {n} - awards, function is over")
                break
