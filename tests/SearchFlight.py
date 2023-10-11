import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchFlight(unittest.TestCase):

    # Punem metoda setupClass pentru ca testele sa-si pastreze valorile intre ele,
    # astfel formularul avand valori complete la trimitere.
    @classmethod
    def setUpClass(self):
        self.firefox = webdriver.Firefox()
        self.firefox.maximize_window()
        self.firefox.get("https://phptravels.site")
        self.firefox.implicitly_wait(30)
        self.firefox.find_element(By.CSS_SELECTOR, 'button[data-bs-target="#tab-flights"]').click()
        self.firefox.implicitly_wait(30)

    def test_1_flying_from_element(self):
        # Testam campul 'from', cautandu-l dupa XPATH, ii dam valoare si verificam ca are valoare oferita.
        from_element = self.firefox.find_element(By.XPATH, '//*[@id="onereturn"]/div[1]/div[1]/div[2]')
        from_element.click()
        from_search_input = self.firefox.find_element(By.XPATH, '//*[@id="fadein"]/span/span/span[1]/input')
        from_search_input.click()
        from_search_input.send_keys('BER')
        time.sleep(2)
        from_search_input.send_keys(Keys.ENTER)
        time.sleep(1)
        from_search_input_value = self.firefox.find_element(By.XPATH, '//*[@id="select2--container"]/div/small/strong')
        self.assertEqual(from_search_input_value.text, 'BER')

    def test_2_destination_to_element(self):
        # Testam campul 'to', cautandu-l dupa XPATH, ii dam valoare si verificam ca are valoare oferita.
        to_element = self.firefox.find_element(By.XPATH, '//*[@id="onereturn"]/div[2]/div[2]/div[2]')
        to_element.click()
        to_search_input = self.firefox.find_element(By.XPATH, '//*[@id="fadein"]/span/span/span[1]/input')
        to_search_input.click()
        to_search_input.send_keys('DXB')
        time.sleep(2)
        to_search_input.send_keys(Keys.ENTER)
        time.sleep(1)
        to_search_input_value = self.firefox.find_element(By.XPATH, '//*[@id="select2--container"]/div[contains(text(), "Dubai")]')
        self.assertEqual(to_search_input_value.text, 'Dubai DXB')

    def test_3_departure_element(self):
        # Testam campul 'Depart', cautandu-l dupa nume, ii dam valoare si verificam ca are valoare oferita.
        departure = self.firefox.find_element(By.NAME, 'depart')
        departure.clear()
        departure.send_keys('01-12-2023')
        self.assertEqual(departure.get_attribute('value'), '01-12-2023')

    def test_4_submit(self):
        # Trimitem formularul si verificam ca suntem pe pagina de rezultate.
        departure = self.firefox.find_element(By.CLASS_NAME, 'search_button')
        departure.click()
        WebDriverWait(self.firefox, 1000).until(EC.title_contains('Flights Result'))
        self.assertEqual(self.firefox.title, 'Flights Result')

    @classmethod
    def tearDownClass(self):
        self.firefox.quit()