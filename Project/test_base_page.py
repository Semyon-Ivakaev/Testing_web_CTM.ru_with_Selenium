import time
import pytest
from .pages.main_page import MainPage
from .pages.history_page import HistoryPage
from .pages.awards_page import AwardsPage
from .pages.smi_page import SMIPage
from .pages.training_page import TraininigPage
from .pages.documents_page import DocumentsPage
from .pages.news_page import NewsPage
from .pages.company_page import CompanyPage


class TestUser:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        pass

    @pytest.mark.skip
    def test_guest_look_base_page(self, browser):
        link = 'https://www.ctm.ru/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8'
        page = MainPage(browser, link)
        page.open()
        time.sleep(1)
        page.guest_look_base_page()
        time.sleep(1)

    @pytest.mark.skip
    def test_guest_look_menu(self, browser):
        link = 'https://www.ctm.ru/'
        page = MainPage(browser, link)
        page.open()
        page.guest_look_menu()

    @pytest.mark.skip
    def test_guest_look_submenu_company(self, browser):
        link = 'https://www.ctm.ru/'
        page = MainPage(browser, link)
        page.open()
        page.guest_look_submenu_company()

    @pytest.mark.skip
    def test_guest_look_submenu_news(self, browser):
        link = 'https://www.ctm.ru/'
        page = MainPage(browser, link)
        page.open()
        page.guest_look_submenu_news()

    @pytest.mark.skip
    def test_guest_look_submenu_products(self, browser):
        link = 'https://www.ctm.ru/'
        page = MainPage(browser, link)
        page.open()
        page.guest_look_submenu_products()

    @pytest.mark.skip
    def test_guest_look_submenu_prices(self, browser):
        link = 'https://www.ctm.ru/'
        page = MainPage(browser, link)
        page.open()
        page.guest_look_submenu_prices()

    @pytest.mark.skip
    def test_guest_look_submenu_contacts(self, browser):
        link = 'https://www.ctm.ru/'
        page = MainPage(browser, link)
        page.open()
        page.guest_look_submenu_contacts()

    @pytest.mark.skip
    def test_guest_look_news_on_base_page(self, browser):
        link = 'https://www.ctm.ru/'
        page = MainPage(browser, link)
        page.open()
        page.guest_look_news_company_on_base_page()
        page.guest_look_news_JD_on_base_page()
        page.guest_look_news_VAD_on_base_page()

    @pytest.mark.skip
    def test_guest_look_services_on_base_page(self, browser):
        link = 'https://www.ctm.ru/'
        page = MainPage(browser, link)
        page.open()
        page.guest_look_services_on_base_page()

    @pytest.mark.skip
    def test_guest_look_programms_on_base_page(self, browser):
        link = 'https://www.ctm.ru/'
        page = MainPage(browser, link)
        page.open()
        page.guest_look_programms_on_base_page()

    @pytest.mark.skip
    def test_guest_look_promo_on_base_page(self, browser):
        link = 'https://www.ctm.ru/'
        page = MainPage(browser, link)
        page.open()
        page.guest_look_promo_on_base_page()

    @pytest.mark.skip
    def test_guest_look_menu_under_on_base_page(self, browser):
        link = 'https://www.ctm.ru/'
        page = MainPage(browser, link)
        page.open()
        page.guest_look_menu_company_under_on_base_page()
        page.guest_look_menu_news_under_on_base_page()
        page.guest_look_menu_products_under_on_base_page()
        page.guest_look_menu_prices_under_on_base_page()
        page.guest_look_menu_contacts_under_on_base_page()

    @pytest.mark.skip
    def test_history_page(self, browser):#этот тест надо дорабатывать
        link = 'https://www.ctm.ru/%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F/%D0%B8%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F'
        page = HistoryPage(browser, link)
        page.open()
        page.should_be_href_on_page()

    @pytest.mark.skip
    def test_guest_look_promo_on_base_page(self, browser):
        link = 'https://www.ctm.ru/%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F/%D0%BD%D0%B0%D0%B3%D1%80%D0%B0%D0%B4%D1%8B'
        page = AwardsPage(browser, link)
        page.open()
        page.guest_look_awards()

    @pytest.mark.skip
    def test_guest_look_smi_about(self, browser):
        link = 'https://www.ctm.ru/%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F/%D1%81%D0%BC%D0%B8'
        page = SMIPage(browser, link)
        page.open()
        page.guest_look_smi_about()

    @pytest.mark.skip
    def test_guest_look_pages_training(self, browser):
        link = 'https://www.ctm.ru/%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F/%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5'
        page = TraininigPage(browser, link)
        page.open()
        page.guest_look_pages_training()

    @pytest.mark.skip
    def test_guest_look_link_on_documents(self, browser):
        link = 'https://www.ctm.ru/documents'
        page = DocumentsPage(browser, link)
        page.open()
        page.guest_look_link_on_documents()

    @pytest.mark.skip
    def test_guest_look_news_on_news_page(self, browser):
        link = 'https://www.ctm.ru/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8'
        page = NewsPage(browser, link)
        page.open()
        page.guest_look_news_on_news_page()

    def test_guest_look_news_on_company_page(self, browser):
        link = 'https://www.ctm.ru/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F'
        page = CompanyPage(browser, link)
        page.open()
        page.guest_look_news_on_company_page()