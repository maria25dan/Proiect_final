from seleniumbase import Driver


class Browser:
    driver = Driver(browser="chrome", headless=False)
    driver.maximize_window()
