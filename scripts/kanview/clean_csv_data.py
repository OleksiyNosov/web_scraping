import os

def csv_to_matrix(filename):
  with open(os.getcwd() + filename, "r") as file:
    lines = file.read().split("\n")

    return [line.split(",") for line in lines[:-1]]

def print_data_sampel(headers, elements, limit = 1):
  if limit > len(elements):
    limit = len(elements)

  for element in elements[0:limit]:
    for i in range(len(headers)):
      print(i, "->", headers[i], "->", element[i])

def clean_feature(elements, feature_index, action):
  for element in elements:
    element[feature_index] = action(element[feature_index])

  return elements


laptops_filename = "scraped_data/laptops.csv"

# Prepare data
elements = csv_to_matrix(laptops_filename)
headers = elements.pop(0)

# Prepare additional attributes
elements_amount = len(elements)
headers_amount = len(headers)


delete_all_spaces = lambda str: str.replace(" ", "")

print_data_sampel(headers, elements)

clean_feature(elements, 23, delete_all_spaces)

print_data_sampel(headers, elements)
