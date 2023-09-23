import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login(unittest.TestCase):

    # Date Utilizator inactive
    LOGIN_EMAIL_INACTIVE = 'ioanaburca9@gmail.com'
    LOGIN_PASSWORD_INACIVE = '123456'

    # Date Utilizator Active
    LOGIN_EMAIL_ACTIVE = 'agent@phptravels.com'
    LOGIN_PASSWORD_ACTIVE = 'demoagent'

    def setUp(self):
        self.firefox = webdriver.Firefox()
        self.firefox.maximize_window()
        self.firefox.get("https://www.phptravels.net/")
        self.firefox.implicitly_wait(5)

    def test_login_page(self):
        # Mergem pe pagina de Login
        self.firefox.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/a').click()
        self.firefox.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/ul/li[1]/a').click()

        # Verificam URL-ul sa fie pe pagina de Login
        current_url = self.firefox.current_url
        expected_url = 'https://phptravels.net/login'
        self.assertTrue(current_url, expected_url)

    def test_inactive_account(self):
        # Mergem pe pagina de Login
        self.firefox.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/a').click()
        self.firefox.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/ul/li[1]/a').click()

        # Dam Valoare elementului email
        email_element = self.firefox.find_element(By.ID, 'email')
        email_element.send_keys(self.LOGIN_EMAIL_INACTIVE)

        # Dam Valoare elementului password
        password_element = self.firefox.find_element(By.ID, 'password')
        password_element.send_keys(self.LOGIN_PASSWORD_INACIVE)

        # Verificam ca apare mesajul Invalid Login.
        self.firefox.find_element(By.ID, 'submitBTN').click()
        account_not_active = self.firefox.find_element(By.XPATH, "//*[contains(text(), 'Inv n')]")
        self.assertTrue(account_not_active)

    def test_active_account(self):
        # Mergem pe pagina de Login
        self.firefox.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/a').click()
        self.firefox.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/ul/li[1]/a').click()

        # Dam Valoare elementului email
        email_element = self.firefox.find_element(By.ID, 'email')
        email_element.send_keys(self.LOGIN_EMAIL_ACTIVE)

        # Dam Valoare elementului password
        password_element = self.firefox.find_element(By.ID, 'password')
        password_element.send_keys(self.LOGIN_PASSWORD_ACTIVE)

        # Verificam ca apare mesajul numele Demo Agent, numele utilizatorului.
        self.firefox.find_element(By.ID, 'submitBTN').click()
        agent_name_expected = 'Demo Agent'
        agent_name_element = self.firefox.find_element(By.XPATH, "//*[@id='fadein']/div[1]/div/div/div[1]/div/div/div/div[3]/h6/strong")
        self.assertEqual(agent_name_element.text, agent_name_expected)
    
    def tearDown(self):
        self.firefox.quit()
