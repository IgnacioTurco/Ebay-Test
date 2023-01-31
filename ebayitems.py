import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from distutils.version import LooseVersion

class EbayItems:
    def __init__(self, my_driver):
        self.select_product = (By.XPATH, '//*[@id="x-refine__group_1__1"]/ul/li[7]/div/a/div/span/input')
        self.driver = my_driver
        self.shoe_size = (By.CSS_SELECTOR, '[aria-label="10"]')
        self.total_results = (By.XPATH, '//*[@id="mainContent"]/div[1]/div/div[2]/div[1]/div[1]/h1')
        self.precios = (By. XPATH, '//span[contains(text(),"USD")][@class="s-item__price"]')

    def click_puma(self):
        self.driver.find_element(*self.select_product).click()
    def click_size(self):
        self.driver.find_element(*self.shoe_size).click()
    def results(self):
        text = self.driver.find_element(*self.total_results).text
        print(text)

    def prices(self):
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=shoes&_sacat=0&Brand=PUMA&rt=nc&US%2520Shoe%2520Size=10&_dcat=93427'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        price = soup.find_all("span", class_="s-item__price")

        precios = list()
        for i in price:
            precios.append(i.contents[0])
        print(precios)

        lista = precios
        del precios[0]
        precios = [precios[i].strip('USD') for i in range(len(precios))]

        new_list = []
        for precio in precios:
             new_list.append(float(precio))
        print(new_list)

        print('lista ordenada')

        new_list.sort()

        print(new_list)
        
        tc = unittest.TestCase('__init__')
        tc.assertTrue(new_list[0] <= new_list[1] <= new_list[2] <= new_list[3] <= new_list[4])

    def first_five_products(self):
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=shoes&_sacat=0&Brand=PUMA&rt=nc&US%2520Shoe%2520Size=10&_dcat=93427'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        #nombres
        name = soup.find_all("div", class_= "s-item__title")
        productos = list()
        count = 0
        for i in name:
            if count < 6:
                productos.append(i.text)
            else:
                break
            count += 1
        del productos[0]
        print(productos, len(productos))
    
        #precios
        price = soup.find_all("span", class_="s-item__price")
        precios = list()
        count = 0
        for i in price:
            if count < 6:
                precios.append(i.text)
            else:
                break
            count += 1
        del precios[0]
        print(precios, len(precios))

        df = pd.DataFrame({'Nombre': productos, 'Precio': precios}, index=list(range(1,6)))

        final_df = df.sort_values(by=['Nombre'])
        print(final_df)

        finals_df = np.vectorize(LooseVersion)
        new_df = df.sort_values('Precio', key= finals_df)
        print(new_df)


    