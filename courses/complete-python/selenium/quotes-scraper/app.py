from selenium import webdriver

from pages.quotes_page import QuotesPage

URL = 'https://quotes.toscrape.com'

# On Linux
# chrome = webdriver.Chrome(executable_path='../chromedriver/chromedriver')

# On Windows
chrome = webdriver.Chrome(executable_path='../chromedriver/chromedriver.exe')

chrome.get(URL)
page = QuotesPage(chrome)

for quote in page.quotes:
    print(quote)
