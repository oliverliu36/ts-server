from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import os

def local_driver():
    driver = webdriver.Chrome()
    return driver

def heroku_platform_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    service = Service(executable_path=os.environ.get("CHROMEDRIVER_PATH"))
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def get_driver():
    # return local_driver()
    return heroku_platform_driver()