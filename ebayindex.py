from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

class EbayIndex:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.query_top = (By.ID, 'gh-ac')
        self.query_button = (By.CLASS_NAME, 'btn btn-prim gh-spr')
        self.busqueda_click = (By.XPATH, '//*[@id="gh-btn"]')

    def search(self, item):
        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.query_top)).send_keys(item)
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.query_button)).click()

        try:
            search_box = WebDriverWait(self.driver, 4).until(EC.presence_of_element_located(self.query_top))
            search_box.send_keys(item)
            search_button = WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(self.query_button))
            search_button.click()
        except:
            print('')

    def click_busqueda(self):
        #self.driver.find_element(*self.busqueda_click).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.busqueda_click)).click()