from seleniumbase import Driver


class Browser:
    def open_browser(self):
        driver = Driver(browser="chrome", headless=False)
        driver.maximize_window()
        return driver
