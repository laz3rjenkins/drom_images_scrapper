import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import urllib
import urllib.request

import constants


class BotScrapper(webdriver.Chrome):
    def __init__(self, driver_path="chromedriver/chromedriver.exe",
                 teardown=False):
        self.options = None
        self.driver_path = driver_path
        self.teardown = teardown
        self.get_options()
        super(BotScrapper, self).__init__(executable_path=self.driver_path, options=self.options)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def get_options(self):
        self.options = Options()
        self.options.add_argument("--start-maximized")
        if constants.IS_HEADLESS_ENABLED:
            self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')

    def parse_drom(self):
        self.get(constants.DROM_LINK)
        time.sleep(2)
        try:
            self.click_on_show_more()
            elems = self.find_elements(By.CLASS_NAME, "css-1q61nn")
            for i in range(0, len(list(elems))):
                son_element = elems[i].find_element(By.CSS_SELECTOR, 'img')

                brand_name = elems[i].find_element(By.TAG_NAME, "span").text
                brand_image_url = son_element.get_attribute('src')
                # print(brand_name)
                self.download_image(brand_name, brand_image_url)
        except Exception as e:
            print(e)

    def click_on_show_more(self):
        elem = self.find_element(By.XPATH,
                                 "/html/body/div[2]/div[5]/div/div[1]/div[3]/div/div[4]/div[5]/div/span/div[1]")
        elem.click()

    def download_image(self, name, url) -> None:
        urllib.request.urlretrieve(str(url), 'images/' + str(name).lower() + '.png')


if __name__ == "__main__":
    bot = BotScrapper()
    bot.parse_drom()
