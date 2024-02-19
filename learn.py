import time
import os
import requests

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def download_images(url, save_folder):
    driver = webdriver.Chrome()

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    images = driver.find_elements(By.XPATH,"//div[@class='mx-auto container-fluid px-0']//img")

    for index, image in enumerate(images):
        actions = ActionChains(driver)
        actions.move_to_element(image).perform()
        time.sleep(0.5)
        full_src = image.get_attribute('src')
        img_response = requests.get(full_src, stream=True)
        if img_response.status_code == 200:
            # 构造图片保存的路径
            path = os.path.join(save_folder, f'image_{index}.jpg')
            # 保存图片
            with open(path, 'wb') as f:
                for chunk in img_response:
                    f.write(chunk)
            print(f'图片已下载：{path}')
        else:
            print(f'图片下载失败：{full_src}')
    driver.close()
