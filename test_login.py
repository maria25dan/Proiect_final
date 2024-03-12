import time
from unittest import TestCase
from selenium.webdriver.common.by import By
import selectors_list
from base_page import BasePage


class TestLogin(TestCase, BasePage):
    def setUp(self):
        print(f"Se executa ce este in setUp() pentru {self._testMethodName}")
        self.driver.get(selectors_list.LINK)
        self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()
        time.sleep(1)

    def tearDown(self):
        print(f"Se executa ce este in tearDown() pentru {self._testMethodName}\n")
        self.driver.quit()


# ● Test 5
# - Lasă goale user și pass
# - Click login
# - Verifică dacă eroarea e displayed

    def test_empty_user_pass(self):
        print(f"A inceput testul {self._testMethodName}")
        login = self.driver.find_element(*selectors_list.LOGIN)
        login.click()
        error_message = self.driver.find_element(*selectors_list.FLASH)
        assert error_message.is_displayed(), f"Error: the error is displayed. "

# ● Test 6
# - Completează cu user și pass invalide
# - Click login
# - Verifică dacă mesajul de pe eroare e corect

    def test_invalid_user_pass(self):
        print(f"A inceput testul {self._testMethodName}")
        user_field = self.driver.find_element(*selectors_list.USER_FIELD)
        # user_field.send_keys("blablabla")
        # pass_field = self.driver.find_element(*selectors_list.PASS_FIELD)
        # pass_field.send_keys(12345678)
        # login = self.driver.find_element(*selectors_list.LOGIN)
        # login.click()
        # error_message = self.driver.find_element(*selectors_list.FLASH).text
        # expected = 'Your username is invalid!'
        # self.assertTrue(expected in error_message, 'Error message text is incorrect')

# ● Test 7
# - Lasă goale user și pass
# - Click login
# - Apasă x la eroare
# - Verifică dacă eroarea a dispărut

    def test_verify_login_rejected_when_user_and_pass_empty(self):
        print(f"A inceput testul {self._testMethodName}")
        self.driver.find_element(*selectors_list.LOGIN).click()
        error_message = self.driver.find_element(*selectors_list.FLASH)
        assert error_message.is_displayed(), f"Error: the error is not solved. "

# ● Test 8
# - Ia ca o listă toate //label
# - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
# Password)
# - Aici e ok să avem 2 asserturi

    def test_username_and_pass_text(self):
        print(f"A inceput testul {self._testMethodName}")
        labels = self.driver.find_elements(*selectors_list.LABELS)
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
        self.driver.find_element(*selectors_list.USER_FIELD).send_keys("tomsmith")
        self.driver.find_element(*selectors_list.PASS_FIELD).send_keys("SuperSecretPassword!")
        self.driver.find_element(*selectors_list.LOGIN).click()
        succes_message = self.wait_for_element_to_be_present(*selectors_list.FLASH_SUCCESS)
        assert succes_message.is_displayed()
        succes_message_2 = self.driver.find_element(*selectors_list.FLASH).text
        expected = " secure area!"
        self.assertIsNot(succes_message_2, expected, print(f"Mesajul contine textul:  {expected} "))
# ● Test 10
# - Completează cu user și pass valide
# - Click login
# - Click logout
# - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login

    def test_login_logout(self):
        print(f"A inceput testul {self._testMethodName}")
        user_field = self.driver.find_element(*selectors_list.USER_FIELD).send_keys("tomsmith")
        pass_field = self.driver.find_element(*selectors_list.PASS_FIELD).send_keys("SuperSecretPassword!")
        click_login = self.driver.find_element(*selectors_list.LOGIN).click()
        click_logout = self.driver.find_element(*selectors_list.LOGOUT).click()
        expected_url = "https://the-internet.herokuapp.com/login"
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Invalid URL, expected {expected_url}, but found {actual_url}"
