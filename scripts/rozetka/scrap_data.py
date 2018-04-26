from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from tabulate import tabulate
import re
import pandas as pd
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def write_all_to_file(text, filename):
  # Get current working directory (cwd)
  path = os.getcwd()

  # Open, Write and Close file
  file = open(path + "/data/" + filename, "w")
  file.write(text)
  file.close()

def append_line_to_file(line, filename):
  # Get current working directory (cwd)
  path = os.getcwd()

  # Open, Write and Close file
  file = open(path + "/data/" + filename, "a+")
  file.write(line + "\n")
  file.close()

def normalize_string(string, separator):
  return string.replace("\r\n", " ").replace("\n", " ").strip().replace(separator, " ")

def extract_selenium_elements_text_to_list(driver, path_to_elements, separator = "|"):
  elements = driver.find_elements_by_css_selector(path_to_elements)

  return [normalize_string(element.text, separator) for element in elements]

def retrieve_data_from_page(driver, path_to_elements, i, separator = "|"):
  element = driver.find_elements_by_css_selector(path_to_elements)[i].click()

  element = driver.find_element_by_css_selector("#tabs > li:nth-child(2) > a")
  WebDriverWait(driver, 0).until_not(EC.visibility_of_element_located((By.ID, "overley")))
  element.click()

  data_list = []

  path_to_elements = "#tab_content > div > div > div.clearfix.pp-tab-with-aside-content.pp-characteristics-tab > table > tbody > tr > td"
  data_list += extract_selenium_elements_text_to_list(driver, path_to_elements)

  price_path = "#tab_content > div > div > div.pp-tab-aside-wrap > div > div > div > div:nth-child(2) > div > div.pp-carriage-inner > div.pp-carriage-good-middle > div.pp-carriage-good-middle-inner > div.pp-carriage-good-label-wrap > div > div > span > span"
  data_list += ["price"]
  data_list += extract_selenium_elements_text_to_list(driver, price_path)

  name_path  = "#content-inner-block > div:nth-child(5) > div > header > div.detail-title-code.pos-fix.clearfix > h1"
  data_list += ["name"]
  data_list += extract_selenium_elements_text_to_list(driver, name_path)

  return separator.join(data_list)

def extract_data_from_page_to_file(driver, url, path_to_elements, filename):
  driver.get(url)
  elements = driver.find_elements_by_css_selector(path_to_elements)

  for i in range(len(elements)):
    driver.get(url)

    driver.find_elements_by_css_selector(path_to_elements)

    result = retrieve_data_from_page(driver, path_to_elements, i)

    append_line_to_file(result, filename)


# Start of a script

# Create new firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(5)

for i in range(1, 76):
  url = "https://rozetka.com.ua/notebooks/c80004/filter/page=" + str(i) + "/"
  path_to_elements = "div.g-i-tile-i-title.clearfix a"

  extract_data_from_page_to_file(driver, url, path_to_elements, "laptops.txt")

# End the Selenium browser session
driver.quit()
