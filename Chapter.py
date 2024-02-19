import pictures
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

from learn import download_images


def download(comicNumber, path):

    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get(f'https://dingmanhua.com/comic/{comicNumber}.html')
    links = driver.find_elements(By.XPATH,"//div[@class='col-6 col-lg-3 col-md-4 col-sm-6 d-grid mt-2 mb-2']//a")

    for index, link in enumerate(links):
        name = link.text
        if not os.path.exists(f'{path}/{name}'):
            os.mkdir(f'{path}/{name}')
            download_images(link.get_attribute('href'), f'{path}/{name}')

    driver.close()
download(1541,'pictures')