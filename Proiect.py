import time
import unittest
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Implementează o clasă Login care să moștenească unittest.TestCase
# Gasește elementele în partea de sus folosind ce selectors dorești:
# - setUp()
# - Driver
# https://the-internet.herokuapp.com/
# Click pe Form Authentication
# tearDown()
# Quit browser
#

class Login(TestCase):
    driver = None
    LINK = "https://the-internet.herokuapp.com/"

    def setUp(self):
        print(f"Se executa ce este in setUp() pentru {self._testMethodName}")
        self.driver = webdriver.Chrome()
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

    def test_title(self):
        print(f"A inceput testul {self._testMethodName}")
        expected_title = "The Internet"
        actual_title = self.driver.title
        assert expected_title == actual_title, f"Invalid title, expected {expected_title}, but found {actual_title}"

# ● Test 3
# - Verifică textul de pe elementul xpath=//h2 e corect

    def test_h2_text(self):
        print(f"A inceput testul {self._testMethodName}")
        expected_text = self.driver.find_element(By.XPATH, "//h2").text
        actual_text = "Login Page"
        assert expected_text == actual_text, f"Invalid text, expected {expected_text}, but found {actual_text}"

# ● Test 4
# - Verifică dacă butonul de login este displayed

    def test_login_display(self):
        print(f"A inceput testul {self._testMethodName}")
        login_button = self.driver.find_element(By.XPATH, "//*[@class='fa fa-2x fa-sign-in']")
        self.assertTrue(login_button.is_displayed(), "Butonul de login nu este afișat pe pagina.")

# ● Test 5
# - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

    def test_href_correct(self):
        print(f"A inceput testul {self._testMethodName}")
        element = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/a")
        element_href = element.get_attribute("href")
        self.assertEqual(element_href, 'http://elementalselenium.com/')

# ● Test 6
# - Lasă goale user și pass
# - Click login
# - Verifică dacă eroarea e displayed

    def test_empty_user_pass(self):
        print(f"A inceput testul {self._testMethodName}")
        login = self.driver.find_element(By.XPATH, "//*[@class='radius']")
        login.click()
        error_message = self.driver.find_element(By.XPATH, "//*[@id='flash']")
        assert error_message.is_displayed()

# ● Test 7
# - Completează cu user și pass invalide
# - Click login
# - Verifică dacă mesajul de pe eroare e corect
# - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
# expected = 'Your username is invalid!'
# self.assertTrue(expected in actual, 'Error message text is
# incorrect')

    def test_invalid_user_pass(self):
        print(f"A inceput testul {self._testMethodName}")
        user_field = self.driver.find_element(By.XPATH, "//*[@id='username']")
        user_field.send_keys("blablabla")
        pass_field = self.driver.find_element(By.XPATH, "//*[@id='password']")
        pass_field.send_keys(12345678)
        login = self.driver.find_element(By.XPATH, "//*[@class='radius']")
        login.click()
        error_message = self.driver.find_element(By.XPATH, "//*[@id='flash']").text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in error_message, 'Error message is incorrect')

# ● Test 8
# - Lasă goale user și pass
# - Click login
# - Apasă x la eroare
# - Verifică dacă eroarea a dispărut

    def test_empty_user_pass(self):
        print(f"A inceput testul {self._testMethodName}")
        user_field = self.driver.find_element(By.XPATH, "//*[@id='username']")
        pass_field = self.driver.find_element(By.XPATH, "//*[@id='password']")
        login = self.driver.find_element(By.XPATH, "//*[@class='radius']").click()
        error_message = self.driver.find_element(By.XPATH, "//*[@id='flash']")
        assert error_message.is_displayed()



# ● Test 9
# - Ia ca o listă toate //label
# - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
# Password)
# - Aici e ok să avem 2 asserturi
#

    def test_username_and_pass_text(self):
        print(f"A inceput testul {self._testMethodName}")
        labels = self.driver.find_elements(By.XPATH, "//label[@for]")
        expected_texts = ["Username", "Password"]
        for label in labels:
            text = label.text
        self.assertIn(text, expected_texts, f"Textul de pe {label} este 'Username' si 'Password'.")


# ● Test 10
# - Completează cu user și pass valide
# - Click login
# - Verifică ca noul url CONTINE /secure
# - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
# - Verifică dacă elementul cu clasa=’flash succes’ este displayed
#
# - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’

    def test_valid_user_pass(self):
        print(f"A inceput testul {self._testMethodName}")
        user_field = self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("tomsmith")
        pass_field = self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys("SuperSecretPassword!")
        click_login = self.driver.find_element(By.XPATH, "//*[@class='radius']").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='flash success']")))
        succes_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='flash success']")))
        assert succes_message.is_displayed()
        succes_message_2 = self.driver.find_element(By.XPATH, "//*[@id='flash']").text
        expected = " secure area!"
        self.assertIsNot(succes_message_2, expected, print(f"Mesajul contine textul:  {expected} "))


# ● Test 11
# - Completează cu user și pass valide
# - Click login
# - Click logout
# - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login

    def test_login_logout(self):
        print(f"A inceput testul {self._testMethodName}")
        user_field = self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("tomsmith")
        pass_field = self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys("SuperSecretPassword!")
        click_login = self.driver.find_element(By.XPATH, "//*[@class='radius']").click()
        click_logout = self.driver.find_element(By.XPATH, "//*[@class='button secondary radius']").click()
        expected_url = "https://the-internet.herokuapp.com/login"
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Invalid URL, expected {expected_url}, but found {actual_url}"

#
# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google
# ● Test 12 - brute force password hacking
# - Completează user tomsmith
# - Găsește elementul //h4
# - Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
# potențială parolă.
# - Folosește o structură iterativă prin care să introduci rând pe rând
# parolele și să apeși pe login.
# - La final testul trebuie să îmi printeze fie
# ‘Nu am reușit să găsesc parola’
# ‘Parola secretă este [parola]’