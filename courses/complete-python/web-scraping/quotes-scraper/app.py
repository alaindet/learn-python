import requests

from pages.quotes_page import QuotesPage

URL = 'https://quotes.toscrape.com'

page_content = requests.get(URL).content
page = QuotesPage(page_content)

for quote in page.quotes:
    print(quote)