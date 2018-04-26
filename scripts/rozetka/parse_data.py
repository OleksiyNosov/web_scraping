import os

def file_to_list(filename):
  path = os.getcwd()

  file = open(path + "/scraped_data/" + filename, "r")
  result = file.read()
  file.close()

  return result.split("\n")

separator = "|"
filename = "laptops.txt"
output_filename = "laptops.csv"
elements = []
raw_elements = file_to_list(filename)
all_keys = []
output_result = ""

incorrect_amounts = 0
incorrect_keys    = 0

for raw_element in raw_elements:
  tmp = raw_element.split(separator)

  if len(tmp) % 2 != 0:
    incorrect_amounts += 1
    next

  element = {}
  for i in range(int(len(tmp) / 2)):
    element[tmp[i * 2]] = tmp[i * 2 + 1]

  if "name" in element:
    elements.append(element)
  else:
    incorrect_keys += 1


for element in elements:
  all_keys += element.keys()

keys = list(set(all_keys))

output_result += ",".join(keys) + "\n"

for element in elements:
  output_result += ",".join([element.get(key, "").replace(",", " ") for key in keys]) + "\n"

path = os.getcwd()
file = open(path + "/data/" + output_filename, "w")
file.write(output_result)
file.close()

print("incorrect_amounts", incorrect_amounts)
print("incorrect_keys", incorrect_keys)
print("len", len(elements))
print("all_keys", len(all_keys))
print("keys", keys)
