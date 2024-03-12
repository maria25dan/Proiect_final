from selenium.webdriver.common.by import By

LINK = "https://the-internet.herokuapp.com/"
LOGIN_BUTTON = (By.XPATH, "//*[@class='fa fa-2x fa-sign-in']")
ACTUAL_TEXT = (By.XPATH, "//h2")
ELEMENT_SELENIUM = (By.XPATH, "/html/body/div[3]/div/div/a")
LOGIN = (By.XPATH, "//*[@class='radius']")
FLASH = (By.XPATH, "//*[@id='flash']")
USER_FIELD = (By.XPATH, "//*[@id='username']")
PASS_FIELD = (By.XPATH, "//*[@id='password']")
LABELS = (By.XPATH, "//label[@for]")
FLASH_SUCCESS = (By.XPATH, "//*[@class='flash success']")
LOGOUT = (By.XPATH, "//*[@class='button secondary radius']")