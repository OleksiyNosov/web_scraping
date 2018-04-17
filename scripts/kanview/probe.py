from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from tabulate import tabulate
import re
import pandas as pd
import os

url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"

# Create new firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(90)
driver.get(url)

python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33')
python_button.click()

# Selenium heads the page source Beautiful Soup
soup_Level1 = BeautifulSoup(driver.page_source, 'lxml')

datalist = []
counter = 0

for link in soup_Level1.find_all('a', id=re.compile("^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_")):

  # Selenium visits each Job Title page
  python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(counter))
  python_button.click()

  # Selenium hands of the source of the specific job page to Beautiful Soup
  soup_level2 = BeautifulSoup(driver.page_source, 'lxml')

  # Beautiful Soup grabs the HTML table on the page
  table = soup_level2.find_all('table')[0]

  # Giving the HTML table to pandas to put in a dataframe object
  df = pd.read_html(str(table), header = 0)

  # Store the dataframe in a list
  datalist.append(df[0])

  # Ask Selenium to click the back button
  driver.execute_script("window.history.go(-1)")

  counter += 1

# End the Selenium browser session
driver.quit()

# Combine all pandas dataframes in the list into one big dataframe
result = pd.concat([pd.DataFrame(datalist[i]) for i in range(len(datalist))], ignore_index = True)

# Pretty print to CLI with tabulate
# Converts to an ascii table
print(tabulate(result, headers=["Employee Name","Job Title","Overtime Pay","Total Gross Pay"], tablefmt='psql'))

# Convert padas dataframe to json
json_records = result.to_json(orient = 'records')

# Get current working directory (cwd)
path = os.getcwd()

# Open, Write and Close file
file = open(path + "/fhsu_payroll_data.json", "w")
file.write(json_records)
file.close()
