from selenium import webdriver
import os

url = "https://rozetka.com.ua/prestigio_psb141c01bfp_bk_cis/p28859249/#tab=characteristics"

def write_all_to_file(text, filename):
  # Get current working directory (cwd)
  path = os.getcwd()

  # Open, Write and Close file
  file = open(path + "/scraped_data/" + filename, "w")
  file.write(text)
  file.close()

def extract_selenium_elements_text(driver, path_to_elements, separator = "|"):
  elements = driver.find_elements_by_css_selector(path_to_elements)

  result = separator.join([element.text.replace("\n", " ") for element in elements])

  return result


# Create new firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get(url)

path_to_elements = "#tab_content > div > div > div.clearfix.pp-tab-with-aside-content.pp-characteristics-tab > table > tbody > tr > td"

result = extract_selenium_elements_text(driver, path_to_elements)

write_all_to_file(result, 'quick_run_test' + ".txt")

# End the Selenium browser session
driver.quit()
