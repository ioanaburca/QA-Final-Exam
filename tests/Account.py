import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Account(unittest.TestCase):

    # Date Utilizator Active
    EMAIL = 'agent@phptravels.com'
    PAROLA = 'demoagent'

    def setUp(self):
        self.firefox = webdriver.Firefox()
        self.firefox.maximize_window()
        self.firefox.get("https://phptravels.site/login")
        self.firefox.implicitly_wait(20)

        # Ne Logam
        self.firefox.find_element(By.ID, 'email').send_keys(self.EMAIL)
        self.firefox.find_element(By.ID, 'password').send_keys(self.PAROLA)
        self.firefox.implicitly_wait(10)
        self.firefox.find_element(By.ID, 'submitBTN').click()
        self.firefox.implicitly_wait(60)

    def test_dashboard(self):
        # Testam ca exista butonul Dashboard si ca titlul paginii este Dashboard
        self.firefox.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/a').click()
        self.firefox.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/ul/li[1]/a').click()
        WebDriverWait(self.firefox, 1000).until(EC.title_contains('Dashboard'))
        self.assertEqual(self.firefox.title, 'Dashboard')

    def test_my_bookings(self):
        # Testam ca exista butonul My Bookings si ca titlul paginei este My Bookings
        self.firefox.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/a').click()
        self.firefox.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/ul/li[2]/a').click()
        WebDriverWait(self.firefox, 1000).until(EC.title_contains('My Bookings'))
        self.assertEqual(self.firefox.title, 'My Bookings')

    def test_wallet(self):
        # Testam ca exista butonul Wallet si ca titlul paginei este Wallet
        self.firefox.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/a').click()
        self.firefox.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/ul/li[3]/a').click()
        WebDriverWait(self.firefox, 1000).until(EC.title_contains('Wallet'))
        self.assertEqual(self.firefox.title, 'Wallet')

    def test_profile(self):
        # Testam ca exista butonul Profile si ca titlul paginei este Profile
        self.firefox.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/a').click()
        self.firefox.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/ul/li[4]/a').click()
        WebDriverWait(self.firefox, 1000).until(EC.title_contains('Profile'))
        self.assertEqual(self.firefox.title, 'Profile')

    def test_logout(self):
        # Testam ca exista butonul Logout si ca se schimba titlul in PHPTRAVELS
        self.firefox.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/a').click()
        self.firefox.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/ul/li[6]/a').click()
        WebDriverWait(self.firefox, 1000).until(EC.title_contains('PHPTRAVELS'))
        self.assertEqual(self.firefox.title, 'PHPTRAVELS')

    def tearDown(self):
        self.firefox.quit()
