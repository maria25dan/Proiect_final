import time
from unittest import TestCase

from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin(TestCase):
    LINK = "https://the-internet.herokuapp.com/"
    LOGIN_BUTTON = (By.XPATH, "//*[@class='fa fa-2x fa-sign-in']")
    EXPECTED_TEXT = (By.XPATH, "//h2")
    ELEMENT = (By.XPATH, "/html/body/div[3]/div/div/a")
    LOGIN = (By.XPATH, "//*[@class='radius']")
    FLASH = (By.XPATH, "//*[@id='flash']")
    USER_FIELD = (By.XPATH, "//*[@id='username']")
    PASS_FIELD = (By.XPATH, "//*[@id='password']")
    LABELS = (By.XPATH, "//label[@for]")
    FLASH_SUCCESS = (By.XPATH, "//*[@class='flash success']")
    LOGOUT = (By.XPATH, "//*[@class='button secondary radius']")

    def setUp(self):
        print(f"Se executa ce este in setUp() pentru {self._testMethodName}")
        self.driver = Driver(browser="chrome",headless=False)
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()
        time.sleep(1)

    def tearDown(self):
        print(f"Se executa ce este in tearDown() pentru {self._testMethodName}\n")
        self.driver.quit()

    def wait_for_element_to_be_present(self, element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(EC.presence_of_element_located(element_locator))

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

    def test_login_data(self):
        #print(f"A inceput testul {self._testMethodName}")
        #expected_text = self.driver.find_element(*self.EXPECTED_TEXT)
        #actual_text = "Login Page"
        #assert expected_text == actual_text, f"Invalid text, expected {expected_text}, but found {actual_text}"
        print(f"A inceput subtestul {self._testMethodName}")
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        self.assertTrue(login_button.is_displayed(), "Butonul de login nu este afișat pe pagina.")

# ● Test 4
# - Verifică dacă butonul de login este displayed
# - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

    def test_href_correct(self):
        print(f"A inceput testul {self._testMethodName}")
        element = self.driver.find_element(*self.ELEMENT)
        element_href = element.get_attribute("href")
        self.assertEqual(element_href, 'http://elementalselenium.com/')

# ● Test 5
# - Lasă goale user și pass
# - Click login
# - Verifică dacă eroarea e displayed

    def test_empty_user_pass(self):
        print(f"A inceput testul {self._testMethodName}")
        login = self.driver.find_element(*self.LOGIN)
        login.click()
        error_message = self.driver.find_element(*self.FLASH)
        assert error_message.is_displayed(), f"Error: the error is displayed. "

# ● Test 6
# - Completează cu user și pass invalide
# - Click login
# - Verifică dacă mesajul de pe eroare e corect

    def test_invalid_user_pass(self):
        print(f"A inceput testul {self._testMethodName}")
        user_field = self.driver.find_element(*self.USER_FIELD)
        user_field.send_keys("blablabla")
        pass_field = self.driver.find_element(*self.PASS_FIELD)
        pass_field.send_keys(12345678)
        login = self.driver.find_element(*self.LOGIN)
        login.click()
        error_message = self.driver.find_element(*self.FLASH).text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in error_message, 'Error message text is incorrect')

# ● Test 7
# - Lasă goale user și pass
# - Click login
# - Apasă x la eroare
# - Verifică dacă eroarea a dispărut

    def test_verify_login_rejected_when_user_and_pass_empty(self):
        print(f"A inceput testul {self._testMethodName}")
        user_field = self.driver.find_element(*self.USER_FIELD)
        pass_field = self.driver.find_element(*self.PASS_FIELD)
        login = self.driver.find_element(*self.LOGIN).click()
        error_message = self.driver.find_element(*self.FLASH)
        assert error_message.is_displayed(), f"Error: the error is not solved. "

# ● Test 8
# - Ia ca o listă toate //label
# - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
# Password)
# - Aici e ok să avem 2 asserturi

    def test_username_and_pass_text(self):
        print(f"A inceput testul {self._testMethodName}")
        labels = self.driver.find_elements(*self.LABELS)
        expected_texts = ["Username", "Password"]
        for label in labels:
            text = label.text
        self.assertIn(text, expected_texts, f"Textul de pe {label} este 'Username' si 'Password'.")


# ● Test 9
# - Completează cu user și pass valide
# - Click login
# - Verifică ca noul url CONTINE /secure
# - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
# - Verifică dacă elementul cu clasa=’flash succes’ este displayed
# - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’

    def test_valid_user_pass(self):
        print(f"A inceput testul {self._testMethodName}")
        user_field = self.driver.find_element(*self.USER_FIELD).send_keys("tomsmith")
        pass_field = self.driver.find_element(*self.PASS_FIELD).send_keys("SuperSecretPassword!")
        click_login = self.driver.find_element(*self.LOGIN).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((self.FLASH_SUCCESS)))
        succes_message = wait.until(EC.visibility_of_element_located((self.FLASH_SUCCESS)))
        assert succes_message.is_displayed()
        succes_message_2 = self.driver.find_element(*self.FLASH).text
        expected = " secure area!"
        self.assertIsNot(succes_message_2, expected, print(f"Mesajul contine textul:  {expected} "))
# ● Test 10
# - Completează cu user și pass valide
# - Click login
# - Click logout
# - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login

    def test_login_logout(self):
        print(f"A inceput testul {self._testMethodName}")
        user_field = self.driver.find_element(*self.USER_FIELD).send_keys("tomsmith")
        pass_field = self.driver.find_element(*self.PASS_FIELD).send_keys("SuperSecretPassword!")
        click_login = self.driver.find_element(*self.LOGIN).click()
        click_logout = self.driver.find_element(*self.LOGOUT).click()
        expected_url = "https://the-internet.herokuapp.com/login"
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Invalid URL, expected {expected_url}, but found {actual_url}"