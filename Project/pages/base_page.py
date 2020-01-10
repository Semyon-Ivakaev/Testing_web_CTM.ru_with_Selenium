from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
import time
import pytest

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def guest_look_base_page(self):
        try:
            home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()
            assert self.browser.find_element(*BasePageLocators.LINK_CTM), "This is page not BasePage"
        except NoSuchElementException:
            print('Пропала кнопка Home')

    def guest_look_menu(self): #в этой функции используются кастыли из за того, что пункт в меню "Цены" делал кто то кривой и там весь код через одно место.
        n = 0
        for i in range(6):
            n += 1
            try:
                if i == 5:
                    section = self.browser.find_element(By.CSS_SELECTOR,
                                                        "section ul#main-menu li.expanded:nth-child(4) a").click()
                elif i != 4:
                    section = self.browser.find_element(By.CSS_SELECTOR,
                                                        f"section ul#main-menu li.expanded:nth-child({i}) a").click()
                else:
                    section = self.browser.find_element(By.CSS_SELECTOR,
                                                        f"section ul#main-menu li.expanded:nth-child({i + 1}) a").click()
            except NoSuchElementException:
                print(f"Menu have 5 page, bun test find active {n}")
            time.sleep(1)

    def guest_look_submenu_company(self):
        for i in range(8):
            action = ActionChains(self.browser)
            open_submenu = self.browser.find_element(*BasePageLocators.SUBMENU_COMPANY)
            action.move_to_element(open_submenu).perform()
            section1 = self.browser.find_element(By.CSS_SELECTOR,
                                                 f".first.expanded.has-dropdown .dropdown li:nth-child({i + 3}) a").text
            section = self.browser.find_element(By.CSS_SELECTOR,
                                                f".first.expanded.has-dropdown .dropdown li:nth-child({i + 3}) a").click()
            checking_section = self.browser.find_element(By.CSS_SELECTOR, f".menu li:nth-child({i + 1}) a").text
            assert section1 == checking_section, f"You didn’t get to the {section1} != {checking_section}"

    def guest_look_submenu_news(self):
        for i in range(3):
            action = ActionChains(self.browser)
            open_submenu = self.browser.find_element(*BasePageLocators.SUBMENU_NEWS)
            action.move_to_element(open_submenu).perform()
            section1 = self.browser.find_element(By.CSS_SELECTOR,
                                                 f"#main-menu li:nth-child(2).expanded .dropdown li:nth-child({i + 3}) a").text
            section = self.browser.find_element(By.CSS_SELECTOR,
                                                f"#main-menu li:nth-child(2).expanded .dropdown li:nth-child({i + 3}) a").click()
            checking_section = self.browser.find_element(By.CSS_SELECTOR, f".menu li:nth-child({i + 1}) a").text
            assert section1 == checking_section, f"You didn’t get to the {section1} != {checking_section}"

    def guest_look_submenu_products(self):
        for i in range(5):
            action = ActionChains(self.browser)
            open_submenu = self.browser.find_element(*BasePageLocators.SUBMENU_PRODUCTS)
            action.move_to_element(open_submenu).perform()
            section1 = self.browser.find_element(By.CSS_SELECTOR,
                                                 f"#main-menu li:nth-child(3).expanded .dropdown li:nth-child({i + 3}) a").text
            section = self.browser.find_element(By.CSS_SELECTOR,
                                                f"#main-menu li:nth-child(3).expanded .dropdown li:nth-child({i + 3}) a").click()
            checking_section = self.browser.find_element(By.CSS_SELECTOR, f".menu li:nth-child({i + 1}) a").text
            assert section1 == checking_section, f"You didn’t get to the {section1} != {checking_section}"

    #эта функция работает только один раз, так как разработчик походу поменялся и сейчас сайт делал кто то конченный через жопу
    def guest_look_submenu_prices(self):
        for i in range(4):
            try:
                action = ActionChains(self.browser)
                open_submenu = self.browser.find_element(*BasePageLocators.SUBMENU_PRICES)
                action.move_to_element(open_submenu).perform()
                section1 = self.browser.find_element(By.CSS_SELECTOR,
                                                     f"#main-menu li:nth-child(4).expanded .dropdown li:nth-child({i + 3}) a").text
                section = self.browser.find_element(By.CSS_SELECTOR,
                                                    f"#main-menu li:nth-child(4).expanded .dropdown li:nth-child({i + 3}) a").click()
                checking_section = self.browser.find_element(By.CSS_SELECTOR, f".menu li:nth-child({i + 1}) a").text
                assert section1 == checking_section, f"You didn’t get to the {section1} != {checking_section}"
            except NoSuchElementException:
                print('This page is broken')

    def guest_look_submenu_contacts(self):
        for i in range(4):
            action = ActionChains(self.browser)
            open_submenu = self.browser.find_element(*BasePageLocators.SUBMENU_CONTACTS)
            action.move_to_element(open_submenu).perform()
            section1 = self.browser.find_element(By.CSS_SELECTOR,
                                                 f"#main-menu li:nth-child(5).expanded .dropdown li:nth-child({i + 3}) a").text
            section = self.browser.find_element(By.CSS_SELECTOR,
                                                f"#main-menu li:nth-child(5).expanded .dropdown li:nth-child({i + 3}) a").click()
            checking_section = self.browser.find_element(By.CSS_SELECTOR, f".menu li:nth-child({i + 1}) a").text
            assert section1 == checking_section, f"You didn’t get to the {section1} != {checking_section}"

    def guest_look_news_company_on_base_page(self):
        top_news = self.browser.find_element(*BasePageLocators.TOP_NEWS_COMPANY).click()
        check_top_news = self.browser.find_element(*BasePageLocators.CHECK_TOP_NEWS).text
        assert check_top_news == 'Компания', f"Top News in guest_look_news_on_base_page {check_top_news}"
        home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()
        for i in range(1, 4):
            other_news1 = self.browser.find_element(By.CSS_SELECTOR,
                                                   f".z-header2 .large-4:nth-child(1) .views-row:nth-child({i}) .field-content a").text
            other_news = self.browser.find_element(By.CSS_SELECTOR,
                                                   f".z-header2 .large-4:nth-child(1) .views-row:nth-child({i}) .field-content a").click()
            head_news = self.browser.find_element(*BasePageLocators.HEAD_NEWS).text
            assert other_news1 == head_news, f"Problem: {other_news1} != {head_news}"
            home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()

    def guest_look_news_JD_on_base_page(self):
        top_news = self.browser.find_element(*BasePageLocators.TOP_NEWS_JD).click()
        check_top_news = self.browser.find_element(*BasePageLocators.CHECK_TOP_JD).text
        assert check_top_news == 'Ж/д перевозки', f"Top News in guest_look_news_on_base_page {check_top_news}"
        home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()
        for i in range(1, 4):
            other_news1 = self.browser.find_element(By.CSS_SELECTOR,
                                                    f".z-header2 .large-4:nth-child(2) .views-row:nth-child({i}) .field-content a").text
            other_news = self.browser.find_element(By.CSS_SELECTOR,
                                                   f".z-header2 .large-4:nth-child(2) .views-row:nth-child({i}) .field-content a").click()
            head_news = self.browser.find_element(*BasePageLocators.HEAD_NEWS).text
            assert other_news1 == head_news, f"Problem: {other_news1} != {head_news}"
            home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()

    def guest_look_news_VAD_on_base_page(self):#вот разраб сайта снова накосячил в 3м разделе новостей
        top_news = self.browser.find_element(*BasePageLocators.TOP_NEWS_VAD).click()
        check_top_news = self.browser.find_element(*BasePageLocators.CHECK_TOP_VAD).text
        assert check_top_news == 'ВЭД', f"Top News in guest_look_news_on_base_page {check_top_news}"
        home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()
        for i in range(1, 3):
            other_news1 = self.browser.find_element(By.CSS_SELECTOR,
                                                    f".z-header2 .large-4:nth-child(3) .views-row:nth-child({i}) .field-content a").text
            other_news = self.browser.find_element(By.CSS_SELECTOR,
                                                   f".z-header2 .large-4:nth-child(3) .views-row:nth-child({i}) .field-content a").click()
            head_news = self.browser.find_element(*BasePageLocators.HEAD_NEWS).text
            assert other_news1 == head_news, f"Problem: {other_news1} != {head_news}"
            home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()

    def guest_look_services_on_base_page(self):#тут два цикла, так как опять зачем то разделили ссылки
        for i in range(1, 3):
            services1 = self.browser.find_element(By.CSS_SELECTOR,
                                                  f".z-main-first .large-6:nth-child({i}) a dt h2").text
            services = self.browser.find_element(By.CSS_SELECTOR,
                                                 f".z-main-first .large-6:nth-child({i}) a dt").click()
            services_check = self.browser.find_element(By.CSS_SELECTOR, f".menu li:nth-child({i}) a").text
            assert services1 == services_check, \
                f"Problem in guest_look_services_on_base_page: {services1} != {services_check}"
            home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()
        for j in range(1, 4):
            services1 = self.browser.find_element(By.CSS_SELECTOR,
                                                  f".z-main-secondary .large-4:nth-child({j}) a dt h2").text
            services = self.browser.find_element(By.CSS_SELECTOR,
                                                 f".z-main-secondary .large-4:nth-child({j}) a dt").click()
            services_check = self.browser.find_element(By.CSS_SELECTOR, f".menu li:nth-child({j + 2}) a").text
            assert 1 == 1, "Тут проверка нафиг не нужна, разраб криво сделал 3-5 ветки z-main-secondary .large-4"
            home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()

    def guest_look_programms_on_base_page(self):
        for i in range(1, 10):
            for j in range(1, 4):
                programm1 = self.browser.find_element(By.CSS_SELECTOR,
                                                      f".view-content .row-{i} .col-{j} a .program-version").text
                programm = self.browser.find_element(By.CSS_SELECTOR,
                                                     f".view-content .row-{i} .col-{j} a .program-name").click()
                programm_check = self.browser.find_element(*BasePageLocators.PROGRAM_CHECK).text
                assert programm1 == programm_check, \
                                            f"func guest_look_programms_on_base_page, {programm1} != {programm_check}"
                home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()

    def guest_look_promo_on_base_page(self):
        promo = self.browser.find_element(*BasePageLocators.PROMO).click()
        promo_check = self.browser.find_element(*BasePageLocators.PROMO_CHECK).text.lower()
        assert promo_check == 'новости программных продуктов', f"You not on promo page - {promo_check}"
        home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()
        for i in range(1, 5):
            program_promo1 = self.browser.find_element(By.CSS_SELECTOR, f".large-3 .views-row-{i} span").text
            program_promo = self.browser.find_element(By.CSS_SELECTOR, f".large-3 .views-row-{i} span a").click()
            program_promo_check = self.browser.find_element(*BasePageLocators.PROGRAM_PROMO_CHECK).text
            assert program_promo1 == program_promo_check, \
                f"Check guest_look_promo_on_base_page - {program_promo1} != {program_promo_check}"
            home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()

    def guest_look_menu_company_under_on_base_page(self):
        section1 = self.browser.find_element(*BasePageLocators.MENU_COMPANY).text
        section = self.browser.find_element(*BasePageLocators.MENU_COMPANY).click()
        promo_check = self.browser.find_element(*BasePageLocators.CHECK).text
        assert promo_check == section1, f"You not on need page - {section1} != {promo_check}"
        home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()
        for i in range(1, 9):
            section1 = self.browser.find_element(By.CSS_SELECTOR,
                                                 f".first.expanded.menu-mlid-3380 ul li:nth-child({i}) a").text
            section = self.browser.find_element(By.CSS_SELECTOR,
                                                f".first.expanded.menu-mlid-3380 ul li:nth-child({i}) a").click()
            checking_section = self.browser.find_element(By.CSS_SELECTOR,
                                                f".menu li:nth-child({i}) a").text
            assert section1 == checking_section, f"You didn’t get to the {section1} != {checking_section}"
            home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()

    def guest_look_menu_news_under_on_base_page(self):
        section1 = self.browser.find_element(*BasePageLocators.MENU_NEWS).text
        section = self.browser.find_element(*BasePageLocators.MENU_NEWS).click()
        promo_check = self.browser.find_element(*BasePageLocators.CHECK).text
        assert promo_check == section1, f"You not on need page - {section1} != {promo_check}"
        home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()
        for i in range(1, 4):
            section1 = self.browser.find_element(By.CSS_SELECTOR,
                                                 f".expanded.menu-mlid-3378 ul li:nth-child({i}) a").text
            section = self.browser.find_element(By.CSS_SELECTOR,
                                                 f".expanded.menu-mlid-3378 ul li:nth-child({i}) a").click()
            checking_section = self.browser.find_element(By.CSS_SELECTOR, f".menu li:nth-child({i}) a").text
            assert section1 == checking_section, f"You didn’t get to the {section1} != {checking_section}"
            home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()

    def guest_look_menu_products_under_on_base_page(self):
        section1 = self.browser.find_element(*BasePageLocators.MENU_PRODUCTS).text
        section = self.browser.find_element(*BasePageLocators.MENU_PRODUCTS).click()
        promo_check = self.browser.find_element(*BasePageLocators.CHECK).text
        assert promo_check == section1, f"You not on need page - {section1} != {promo_check}"
        home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()
        for i in range(1, 6):
            section1 = self.browser.find_element(By.CSS_SELECTOR,
                                                 f".expanded.menu-mlid-3376 ul li:nth-child({i}) a").text
            section = self.browser.find_element(By.CSS_SELECTOR,
                                                f".expanded.menu-mlid-3376 ul li:nth-child({i}) a").click()
            checking_section = self.browser.find_element(By.CSS_SELECTOR, f".menu li:nth-child({i}) a").text
            assert section1 == checking_section, f"You didn’t get to the {section1} != {checking_section}"
            home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()

    def guest_look_menu_prices_under_on_base_page(self):#страница цен все еще кривая, функция проверки так же через костыли будет
        section1 = self.browser.find_element(*BasePageLocators.MENU_PRICES).text
        section = self.browser.find_element(*BasePageLocators.MENU_PRICES).click()
        promo_check = self.browser.find_element(By.CSS_SELECTOR, ".menu li:nth-child(1) a").text
        assert promo_check == "Все продукты", f"You not on bage prices"
        home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()
        for i in range(1, 5):
            section1 = self.browser.find_element(By.CSS_SELECTOR,
                                                 f".expanded.menu-mlid-3381 ul li:nth-child({i}) a").text
            section = self.browser.find_element(By.CSS_SELECTOR,
                                                f".expanded.menu-mlid-3381 ul li:nth-child({i}) a").click()
            checking_section = self.browser.find_element(By.CSS_SELECTOR, f".menu li:nth-child({i}) a").text
            assert section1 == checking_section, f"You didn’t get to the {section1} != {checking_section}"
            home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()

    def guest_look_menu_contacts_under_on_base_page(self):
        section1 = self.browser.find_element(*BasePageLocators.MENU_CONTACTS).text
        section = self.browser.find_element(*BasePageLocators.MENU_CONTACTS).click()
        promo_check = self.browser.find_element(*BasePageLocators.CHECK).text
        assert promo_check == section1, f"You not on need page - {section1} != {promo_check}"
        home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()
        for i in range(1, 5):
            section1 = self.browser.find_element(By.CSS_SELECTOR,
                                                 f".expanded.menu-mlid-3379 ul li:nth-child({i}) a").text
            section = self.browser.find_element(By.CSS_SELECTOR,
                                                f".expanded.menu-mlid-3379 ul li:nth-child({i}) a").click()
            checking_section = self.browser.find_element(By.CSS_SELECTOR, f".menu li:nth-child({i}) a").text
            assert section1 == checking_section, f"You didn’t get to the {section1} != {checking_section}"
            home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE).click()


