import time
import pytest
from .locators import *
from selenium import webdriver
from .base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class NewsPage(BasePage):
    def guest_look_news_on_news_page(self):
        n = 0
        for i in range(1, 4):
            header_news = self.browser.find_element(By.CSS_SELECTOR, f".row.collapse .large-4:nth-child({i}) .view-header h2").text
            self.browser.find_element(By.CSS_SELECTOR, f".row.collapse .large-4:nth-child({i}) .view-header h2").click()
            check_header_news = self.browser.find_element(By.CSS_SELECTOR, f".menu li:nth-child({i}) a").text
            assert header_news[:-2] == check_header_news, f"function guest_look_news_on_news_page {header_news} != {check_header_news}"
            self.browser.find_element(By.CSS_SELECTOR, "section ul#main-menu li.expanded:nth-child(2) a").click()
            for j in range(1, 8):
                news = self.browser.find_element(By.CSS_SELECTOR, f".row.collapse .large-4:nth-child({i}) .view-content .views-row:nth-child({j}) a").text
                self.browser.find_element(By.CSS_SELECTOR, f".row.collapse .large-4:nth-child({i}) .view-content .views-row:nth-child({j}) a").click()
                head_news = self.browser.find_element(*BasePageLocators.HEAD_NEWS).text
                assert news == head_news, f"Problem: {news} != {head_news}"
                self.browser.find_element(By.CSS_SELECTOR, "section ul#main-menu li.expanded:nth-child(2) a").click()
                n += 1
        assert i == 3, f"Find {i} header news - must have 3"
        assert n == 21, f"Find {n} news - must have 21"

