import time
import pytest
from .locators import *
from selenium import webdriver
from .base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class CompanyPage(BasePage):
    def guest_look_news_on_company_page(self):
        for i in range(2):
            for j in range(1, 8):
                header_news = self.browser.find_element(By.CSS_SELECTOR, f".view-content .views-row:nth-child({j}) .large-9 a").text
                self.browser.find_element(By.CSS_SELECTOR, f".view-content .views-row:nth-child({j}) .large-9 a").click()
                check_header_news = self.browser.find_element(*BasePageLocators.HEAD_NEWS).text
                assert header_news == check_header_news, f"function guest_look_news_on_company_page {header_news} != {check_header_news}"
                action = ActionChains(self.browser)
                open_submenu = self.browser.find_element(*BasePageLocators.SUBMENU_NEWS)
                action.move_to_element(open_submenu).perform()
                section1 = self.browser.find_element(By.CSS_SELECTOR, "#main-menu li:nth-child(2).expanded .dropdown li:nth-child(3) a").click()
            self.browser.find_element(*BasePageLocators.BUTTON_NEXT).click()