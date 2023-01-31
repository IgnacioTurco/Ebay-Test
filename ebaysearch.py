import unittest
from selenium import webdriver
from ebayindex import EbayIndex
from ebayitems import EbayItems
from selenium.webdriver.chrome.options import Options


class Ebaysearch(unittest.TestCase):
    def setUp(self):
        option = Options()
        option.add_argument("--headless")
        option.add_argument('start-maximized')
        self.driver = webdriver.Chrome('Chromedriver.exe', options = option)
        self.driver.get('https://www.ebay.com/')
        self.driver.implicitly_wait(5)
        self.ebayindex = EbayIndex(self.driver)
        self.ebayitems = EbayItems(self.driver)


    def test_case(self):
        self.ebayindex.search('shoes')
        self.ebayindex.click_busqueda()
        self.ebayitems.click_puma()
        self.ebayitems.click_size()
        self.ebayitems.results()
        self.ebayitems.prices()
        self.ebayitems.first_five_products()



    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()