import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home(unittest.TestCase):
    def setUp(self):
        self.firefox = webdriver.Firefox()
        self.firefox.maximize_window()
        self.firefox.get("https://phptravels.site/")
        self.firefox.implicitly_wait(5)

    def test_hotel_area_section(self):
        # Testam ca exista sectiunea cu clasa hotel-area
        hotel_area_section = self.firefox.find_element(By.CLASS_NAME, 'hotel-area')
        self.assertTrue(hotel_area_section)

        # Daca exista sectiunea, testam ca exista carouselul
        if hotel_area_section:
            carousel = self.firefox.find_element(By.CLASS_NAME, 'featured--hotels-slick')
            self.assertTrue(carousel)

            # Daca exista carouselul, testam ca putem da click pe butonul cu clasa slick-prev
            if carousel:
                carousel_prev = self.firefox.find_element(By.CLASS_NAME, 'slick-prev')
                carousel_prev.location_once_scrolled_into_view
                WebDriverWait(self.firefox, 10000).until(EC.element_to_be_clickable(carousel_prev))
                carousel_prev.click()
                prev_clicked = True;
                self.assertTrue(prev_clicked)

    def test_flights_section(self):
        # Testam ca exista sectiunea cu clasa round-trip-flight
        featured_flights_section = self.firefox.find_element(By.CLASS_NAME, 'round-trip-flight')
        self.assertTrue(featured_flights_section)

        # Testam ca exista elementul cu clasa price-box
        price = self.firefox.find_elements(By.CLASS_NAME, 'price-box')
        price_len = len(price) > 0
        self.assertTrue(price_len)

    def test_tablist(self):
        # Testam ca elementele din lista cu id-ul tab au clasa nav-item
        tab_parent = self.firefox.find_element(By.XPATH, "//*[@id='tab']")
        nav_tabs = tab_parent.find_elements(By.XPATH, '*')
        for nav_tab in nav_tabs:
            nav_tab_class = nav_tab.get_attribute('class')
            self.assertEqual(nav_tab_class, 'nav-item')

    def tearDown(self):
        self.firefox.quit()
