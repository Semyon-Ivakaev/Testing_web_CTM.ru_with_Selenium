import time
import pytest
from .locators import *
from selenium import webdriver
from .base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class TraininigPage(BasePage):
    def guest_look_pages_training(self):
        n = 0
        for i in range(1, 100):
            try:
                look1 = self.browser.find_element(By.CSS_SELECTOR,
                                                         f".view-content div:nth-child({i}) h2 a").text
                look = self.browser.find_element(By.CSS_SELECTOR, \
                                                        f".view-content div:nth-child({i}) h2 a").click()
                look_training_check = self.browser.find_element(*TrainingPageLocators.TRAINING_TITLE).text
                assert look1 == look_training_check, f"guest_look_pages_training error {look1} != {look_training_check}"
                action = ActionChains(self.browser)
                open_submenu = self.browser.find_element(*BasePageLocators.SUBMENU_COMPANY)
                action.move_to_element(open_submenu).perform()
                section = self.browser.find_element(By.CSS_SELECTOR,
                                                    ".first.expanded.has-dropdown .dropdown li:nth-child(9) a").click()
                n += 1
            except NoSuchElementException:
                print(f"Test Find {n} - training_page, function is over")
                break