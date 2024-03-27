from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import requests
from io import BytesIO


def parse(url='https://www.wildberries.ru/catalog/195788158/detail.aspx', index=''):
    """ Func that parse information from url (wildberries)

    Images saves in \data, return price.
    :param url: link for card of product
    :param index: file_name{index}.png
    :return: current price in str, src of photo

    """
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(5)


    photo = driver.find_element(by=By.CLASS_NAME, value='photo-zoom__preview')
    photo_src = photo.get_attribute('src')
    save_img(photo_src, index)

    history = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "price-history"))).screenshot_as_png
    with open(f'C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\parser\\history{index}.png', 'wb') as f:
        f.write(history)

    price = driver.find_element(by=By.CLASS_NAME, value='price-block__final-price')


    # driver.quit()
    return price.text, photo_src


def save_img(src, index):
    response = requests.get(src)

    if response.status_code == 200:
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.save(f'C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\parser\\item_photo{index}.png')
    else:
        print("Error downloading image")
