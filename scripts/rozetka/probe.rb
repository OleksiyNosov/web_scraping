require 'httparty'
require 'nokogiri'

def write_page_to_file url, filename = 'temp_response.html'
  response = HTTParty.get(url)

  File.open(filename, 'w') { |file| file.write(response) }
end

def read_from_file filename = 'temp_response.html'
  File.read(filename)
end

page = 1
url = "https://rozetka.com.ua/notebooks/c80004/filter/page=#{ page };view=list/"
filename = 'temp_response.html'

write_page_to_file(url)

response = read_from_file 'temp_response.html'

parsed_response = Nokogiri::HTML(response)

result = parsed_response.css('#catalog_goods_block')

result.search('script').remove

i = 0

result = result.children.map do |element|
  output = []

  i += 1

  output << "\n--------------------------------------------------------------------------------------------------------------\n"
  output << element.to_s
  output << element.css('div.over-wraper.g-i-list-title>a[href].underline').text.strip

  output.join(',')
end

File.open('temp.csv', 'w') { |file| file.write(result.join("\n")) }

puts "#{ i } cycles"


