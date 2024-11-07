import os
import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv


load_dotenv()
USER_DATA_DIR = os.environ.get("USER_DATA_DIR")
GOOGLE_FORM_LINK = os.environ.get("GOOGLE_FORM_LINK")

def fill_form(address: str, price: str, link: str) -> None:
    """
    Fills out my google form for collecting Zillow property data

    :param address: address for Zillow property
    :type address: str
    :param price: price for Zillow property
    :type price: str
    :param link: link for Zillow property
    :type link: str
    """
    chrome_options= webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(GOOGLE_FORM_LINK)

    # wait 5 seconds before filling
    time.sleep(5)
    
    # find input fields to enter data
    input_fields = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    # I have 3 fields
    input_fields[0].send_keys(address)
    input_fields[1].send_keys(price)
    input_fields[2].send_keys(link)
    
    # after everything is filled out, submit
    submit_button = driver.find_element(By.CSS_SELECTOR, "div[role='button']")
    submit_button.click()
