import time
from unittest import TestCase
from selenium.webdriver.common.by import By
import selectors
from base_page import BasePage


class TestLogin(TestCase, BasePage):

    def setUp(self):
        print(f"Se executa ce este in setUp() pentru {self._testMethodName}")
        self.driver.get(selectors.LINK)
        self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()
        time.sleep(1)

    def tearDown(self):
        print(f"Se executa ce este in tearDown() pentru {self._testMethodName}\n")
        self.driver.quit()

# ● Test 1
# - Verifică dacă noul url e corect

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
        actual_text = self.driver.find_element(selectors.ACTUAL_TEXT).text
        expected_text = "Login Page"
        assert expected_text == actual_text, f"Invalid text, expected {expected_text}, but found {actual_text}"
        print(f"A inceput subtestul {self._testMethodName}")
        login_button = self.driver.find_element(selectors.LOGIN_BUTTON)
        self.assertTrue(login_button.is_displayed(), "Butonul de login nu este afișat pe pagina.")

# ● Test 4
# - Verifică dacă butonul de login este displayed
# - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

    def test_href_correct(self):
        print(f"A inceput testul {self._testMethodName}")
        element = self.driver.find_element(selectors.ELEMENT)
        element_href = element.get_attribute("href")
        self.assertEqual(element_href, 'http://elementalselenium.com/')

# ● Test 5
# - Lasă goale user și pass
# - Click login
# - Verifică dacă eroarea e displayed

    def test_empty_user_pass(self):
        print(f"A inceput testul {self._testMethodName}")
        login = self.driver.find_element(selectors.LOGIN)
        login.click()
        error_message = self.driver.find_element(selectors.FLASH)
        assert error_message.is_displayed(), f"Error: the error is displayed. "

# ● Test 6
# - Completează cu user și pass invalide
# - Click login
# - Verifică dacă mesajul de pe eroare e corect

    def test_invalid_user_pass(self):
        print(f"A inceput testul {self._testMethodName}")
        user_field = self.driver.find_element(selectors.USER_FIELD)
        user_field.send_keys("blablabla")
        pass_field = self.driver.find_element(selectors.PASS_FIELD)
        pass_field.send_keys(12345678)
        login = self.driver.find_element(selectors.LOGIN)
        login.click()
        error_message = self.driver.find_element(selectors.FLASH).text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in error_message, 'Error message text is incorrect')

# ● Test 7
# - Lasă goale user și pass
# - Click login
# - Apasă x la eroare
# - Verifică dacă eroarea a dispărut

    def test_verify_login_rejected_when_user_and_pass_empty(self):
        print(f"A inceput testul {self._testMethodName}")
        self.driver.find_element(selectors.LOGIN).click()
        error_message = self.driver.find_element(selectors.FLASH)
        assert error_message.is_displayed(), f"Error: the error is not solved. "

# ● Test 8
# - Ia ca o listă toate //label
# - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
# Password)
# - Aici e ok să avem 2 asserturi

    def test_username_and_pass_text(self):
        print(f"A inceput testul {self._testMethodName}")
        labels = self.driver.find_elements(selectors.LABELS)
        expected_texts = ["Username", "Password"]
        is_label_correct = True

        for i in range(len(labels)):
            if labels[i] != expected_texts[i]:
                is_label_correct = False

        self.assertTrue(is_label_correct is True, f"Textul de pe label nu este corect. Expected: {expected_texts}, "
                                                  f"actual:{labels}")

# ● Test 9
# - Completează cu user și pass valide
# - Click login
# - Verifică daca noul url CONTINE /secure
# - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
# - Verifică dacă elementul cu clasa=’flash succes’ este displayed
# - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’

    def test_valid_user_pass(self):
        print(f"A inceput testul {self._testMethodName}")
        self.driver.find_element(selectors.USER_FIELD).send_keys("tomsmith")
        self.driver.find_element(selectors.PASS_FIELD).send_keys("SuperSecretPassword!")
        self.driver.find_element(selectors.LOGIN).click()
        succes_message = self.wait_for_element_to_be_present(selectors.FLASH_SUCCESS)
        assert succes_message.is_displayed()
        succes_message_2 = self.driver.find_element(selectors.FLASH).text
        expected = " secure area!"
        self.assertIsNot(succes_message_2, expected, print(f"Mesajul contine textul:  {expected} "))
# ● Test 10
# - Completează cu user și pass valide
# - Click login
# - Click logout
# - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login

    def test_login_logout(self):
        print(f"A inceput testul {self._testMethodName}")
        user_field = self.driver.find_element(selectors.USER_FIELD).send_keys("tomsmith")
        pass_field = self.driver.find_element(selectors.PASS_FIELD).send_keys("SuperSecretPassword!")
        click_login = self.driver.find_element(selectors.LOGIN).click()
        click_logout = self.driver.find_element(selectors.LOGOUT).click()
        expected_url = "https://the-internet.herokuapp.com/login"
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Invalid URL, expected {expected_url}, but found {actual_url}"