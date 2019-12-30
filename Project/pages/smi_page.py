import time
import pytest
from .locators import *
from selenium import webdriver
from .base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class SMIPage(BasePage):
    def guest_look_smi_about(self):
        n = 0
        for i in range(1, 100):
            try:
                look1 = self.browser.find_element(By.CSS_SELECTOR,
                                                         f".view-content div:nth-child({i}) .row .large-9 a").text
                look = self.browser.find_element(By.CSS_SELECTOR, \
                                                        f".view-content div:nth-child({i}) .row .large-9 a").click()
                look_check = self.browser.find_element(*SMIPageLocators.SMI_TITLE).text
                assert look1 == look_check, f"guest_look_smi_about error {look} != {look_check}"
                action = ActionChains(self.browser)
                open_submenu = self.browser.find_element(*BasePageLocators.SUBMENU_COMPANY)
                action.move_to_element(open_submenu).perform()
                section = self.browser.find_element(By.CSS_SELECTOR,
                                                    ".first.expanded.has-dropdown .dropdown li:nth-child(5) a").click()
                n += 1
            except NoSuchElementException:
                print(f"Test Find {n} - SMI about, function is over")
                break
