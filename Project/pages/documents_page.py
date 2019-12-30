import time
import pytest
from .locators import *
from selenium import webdriver
from .base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class DocumentsPage(BasePage):
    def guest_look_link_on_documents(self):
        n = 0
        for i in range(1, 100):
            try:
                first_window = self.browser.window_handles[0]
                self.browser.find_element(By.CSS_SELECTOR, f".body ul li:nth-child({i}) a").click()
                new_window = self.browser.window_handles[1]
                assert new_window, "New window dont open in guest_look_link_on_documents"

                self.browser.switch_to.window(new_window)
                self.browser.close()
                self.browser.switch_to.window(first_window)

                n += 1
            except NoSuchElementException:
                print(f"Test Find {n} - link_on_documents, function is over")
                break
