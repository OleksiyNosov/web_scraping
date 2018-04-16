require 'httparty'
require 'nokogiri'

def write_page_to_file url, filename = 'temp_response.html'
  response = HTTParty.get(url)

  File.open(filename, 'w') { |file| file.write(response) }
end

def read_from_file filename = 'temp_response.html'
  File.read(filename)
end

main_url = 'https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_2?_encoding=UTF8&pg='
page = 1
url = "#{ main_url }#{ page }"
filename = 'temp_response.html'

# write_page_to_file(url)

response = read_from_file 'temp_response.html'

parsed_response = Nokogiri::HTML(response)

result = parsed_response.css('#zg-ordered-list')

result = result.children.map do |element|
  output = []

  output << element.css('.zg-badge-text').text.strip
  output << element.css('.p13n-sc-truncate').text.strip
  output << element.css('.a-size-small').text.strip
  output << element.css('.p13n-sc-price').text.strip
  output << element.css('a.a-size-small.a-link-normal').text.strip
  output << element.css('.zg-release-date').text.strip
  output << element.css('.a-size-small.a-color-secondary').text.strip

  output.join('|')
end

File.open('temp.tsv', 'w') { |file| file.write(result.join("\n")) }



