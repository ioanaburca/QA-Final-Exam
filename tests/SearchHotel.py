import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchHotel(unittest.TestCase):

    # Punem metoda setupClass pentru ca testele sa-si pastreze valorile intre ele,
    # astfel formularul avand valori complete la trimitere.
    @classmethod
    def setUpClass(self):
        self.firefox = webdriver.Firefox()
        self.firefox.maximize_window()
        self.firefox.get("https://phptravels.site")
        self.firefox.implicitly_wait(30)

        # Mergem pe tabul Hotels
        self.firefox.find_element(By.CSS_SELECTOR, 'button[data-bs-target="#tab-hotels"]').click()
        self.firefox.implicitly_wait(30)
    def test_1_search_by_element(self):
        # Testam campul 'Search By', cautandu-l dupa XPATH, ii dam valoare si verificam ca are valoare oferita.
        self.firefox.find_element(By.XPATH, '//*[@id="hotels-search"]/div/div[1]/div[1]').click()

        # Dam valoarea elementului.
        search_element = self.firefox.find_element(By.CSS_SELECTOR, 'input[aria-controls="select2-hotels_city-results"]')
        search_element.send_keys('Dubai')
        time.sleep(1)
        search_element.send_keys(Keys.ENTER)
        time.sleep(1)

        # Verificam ca elementul are valoarea introdusa.
        search_value = self.firefox.find_element(By.XPATH, '//*[@id="select2-hotels_city-container"][contains(text(), "Dubai")]')
        self.assertEqual(search_value.text, 'Dubai United Arab Emirates')

    def test_2_checkin_element(self):
        # Testam campul 'Checkin', cautandu-l dupa ID, ii dam valoare si verificam ca are valoare oferita.
        checkin = self.firefox.find_element(By.ID, 'checkin')
        checkin.clear()
        checkin.send_keys('01-12-2023')
        self.assertEqual(checkin.get_attribute('value'), '01-12-2023')

    def test_3_checkout_element(self):
        # Testam campul 'Checkout', cautandu-l dupa ID, ii dam valoare si verificam ca are valoare oferita.
        checkout = self.firefox.find_element(By.ID, 'checkout')
        checkout.clear()
        checkout.send_keys('02-12-2023')
        self.assertEqual(checkout.get_attribute('value'), '02-12-2023')

        # Trimitem formularul, cu functie submit, apelata pe campul de checkout.
        checkout.submit()
        WebDriverWait(self.firefox, 10000).until(EC.title_contains('Hotels'))

        # Verificam ca suntem pe pagina de rezultate de Hoteluri.
        self.assertEqual(self.firefox.title, 'Hotels - Dubai')

    @classmethod
    def tearDownClass(self):
        self.firefox.quit()