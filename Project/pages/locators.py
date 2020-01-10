from selenium.webdriver.common.by import By

class BasePageLocators():
    CHECKING_SECTION = (By.CSS_SELECTOR, "li.current")
    LINK_CTM = (By.CSS_SELECTOR, "link[href='https://www.ctm.ru/']")
    HOME_PAGE = (By.CSS_SELECTOR, "#home")
    SUBMENU_COMPANY = (By.CSS_SELECTOR, "section li:nth-child(1).expanded.has-dropdown")
    MENU_COMPANY = (By.CSS_SELECTOR, ".first.expanded.menu-mlid-3380 a")
    SUBMENU_NEWS = (By.CSS_SELECTOR, "#main-menu li:nth-child(2).expanded")
    MENU_NEWS = (By.CSS_SELECTOR, ".expanded.menu-mlid-3378 a")
    SUBMENU_PRODUCTS = (By.CSS_SELECTOR, "#main-menu li:nth-child(3).expanded")
    MENU_PRODUCTS = (By.CSS_SELECTOR, ".expanded.menu-mlid-3376 a")
    SUBMENU_PRICES = (By.CSS_SELECTOR, "#main-menu li:nth-child(4).expanded")
    MENU_PRICES = (By.CSS_SELECTOR, ".expanded.menu-mlid-3381 a")
    SUBMENU_CONTACTS = (By.CSS_SELECTOR, "#main-menu li:nth-child(5).expanded")
    MENU_CONTACTS = (By.CSS_SELECTOR, ".expanded.menu-mlid-3379 a")
    HEAD_NEWS = (By.CSS_SELECTOR, "h1.title")
    TOP_NEWS_COMPANY = (By.CSS_SELECTOR, f".large-4.columns:nth-child(1) h2 a")
    CHECK_TOP_NEWS = (By.CSS_SELECTOR, f".menu li:nth-child(1) a")
    TOP_NEWS_JD = (By.CSS_SELECTOR, f".large-4.columns:nth-child(2) h2 a")
    CHECK_TOP_JD = (By.CSS_SELECTOR, f".menu li:nth-child(2) a")
    TOP_NEWS_VAD = (By.CSS_SELECTOR, f".large-4.columns:nth-child(3) h2 a")
    CHECK_TOP_VAD = (By.CSS_SELECTOR, f".menu li:nth-child(3) a")
    PROGRAM_CHECK = (By.CSS_SELECTOR, "article .row .large-8 strong")
    PROMO = (By.CSS_SELECTOR, ".large-3 .view-header a")
    PROMO_CHECK = (By.CSS_SELECTOR, ".current a")
    PROGRAM_PROMO_CHECK = (By.CSS_SELECTOR, ".field span")
    CHECK = (By.CSS_SELECTOR, "#main-menu .active")
    RAIL_SUBMENU = (By.CSS_SELECTOR, ".button.tiny i")
    LINK_CHECK = (By.CSS_SELECTOR, "link[rel='canonical']")
    BUTTON_NEXT = (By.CSS_SELECTOR, ".arrow a")

class AwardsPageLocators():
    AWARDS_TITLE = (By.CSS_SELECTOR, "#page-title")

class SMIPageLocators():
    SMI_TITLE = (By.CSS_SELECTOR, "#page-title")

class TrainingPageLocators():
    TRAINING_TITLE = (By.CSS_SELECTOR, "#page-title")