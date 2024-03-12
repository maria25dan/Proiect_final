import unittest
from selenium.webdriver.common.by import By
from utils import selectors_list
from utils.base_page import BasePage


class TestWebsiteMetadata(BasePage, unittest.TestCase):
    def setUp(self):
        print(f"Se executa ce este in setUp() pentru {self._testMethodName}")
        self.driver.get(selectors_list.LINK)
        self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()


    def tearDown(self):
        print(f"Se executa ce este in tearDown() pentru {self._testMethodName}\n")
        self.driver.quit()


#● Test 1
#- Verifică dacă noul url e corect

    def test_url(self):
        print(f"A inceput testul {self._testMethodName}")
        expected_url = "https://the-internet.herokuapp.com/login"
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Invalid URL, expected {expected_url}, but found {actual_url}"

# ● Test 2
# - Verifică dacă page title e corect

    def test_page_title(self):
        print(f"A inceput testul {self._testMethodName}")
        expected_title = "The Internet"
        actual_title = self.driver.title
        assert expected_title == actual_title, f"Invalid title, expected {expected_title}, but found {actual_title}"

# ● Test 3
# - Verifică dacă textul de pe elementul xpath=//h2 e corect

    def test_login_data_verify_login_display(self):
        print(f"A inceput testul {self._testMethodName}")
        actual_text = self.driver.find_element(selectors_list.ACTUAL_TEXT).text
        expected_text = "Login Page"
        assert expected_text == actual_text, f"Invalid text, expected {expected_text}, but found {actual_text}"
        print(f"A inceput subtestul {self._testMethodName}")
        login_button = self.driver.find_element(selectors_list.LOGIN_BUTTON)
        self.assertTrue(login_button.is_displayed(), "Butonul de login nu este afișat pe pagina.")

# ● Test 4
# - Verifică dacă butonul de login este displayed
# - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

    def test_href_correct(self):
        print(f"A inceput testul {self._testMethodName}")
        element = self.driver.find_element(selectors_list.ELEMENT_SELENIUM)
        element_href = element.get_attribute("href")
        self.assertEqual(element_href, 'http://elementalselenium.com/')
