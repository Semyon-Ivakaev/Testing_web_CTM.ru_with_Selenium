import time
import pytest
from .locators import *
from selenium import webdriver
from .base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class HistoryPage(BasePage):
    def should_be_href_on_page(self):
        for i in range(1, 20):
            for j in range(1, 20):
                try:
                    if self.browser.find_element(By.CSS_SELECTOR, f".body p:nth-child({i}) a:nth-child({j})").text:
                        find_href1 = self.browser.find_element(By.CSS_SELECTOR, f".body p:nth-child({i}) a:nth-child({j})").text
                        find_href = self.browser.find_element(By.CSS_SELECTOR, f".body p:nth-child({i}) a:nth-child({j})").click()
                        find_href_check = self.browser.find_element(By.CSS_SELECTOR, "#page-title").text
                        assert find_href1.strip('«, »') in find_href_check, f"Error {find_href1.strip('«, »')} != {find_href_check}"
                        time.sleep(1)
                        action = ActionChains(self.browser)
                        open_submenu = self.browser.find_element(*BasePageLocators.SUBMENU_COMPANY)
                        action.move_to_element(open_submenu).perform()
                        section = self.browser.find_element(By.CSS_SELECTOR,
                                                            ".first.expanded.has-dropdown .dropdown li:nth-child(3) a").click()
                except NoSuchElementException:
                    continue




