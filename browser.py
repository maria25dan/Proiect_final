from seleniumbase import Driver


class Browser:
    def open_browser(self):
        self.driver = Driver(browser="chrome", headless=False)
        self.driver.maximize_window()