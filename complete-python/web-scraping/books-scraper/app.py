import requests

from pages.all_books_page import AllBooksPage

BOOKS_URL = 'https://books.toscrape.com'
TEMP_FILE = 'books.temp'
page_content = ''

try:
    with open(TEMP_FILE, 'r') as file:
        page_content = file.read()
except FileNotFoundError: 
    page_content = requests.get(BOOKS_URL).text
    with open(TEMP_FILE, 'w') as file:
        file.write(page_content)

all_books_page = AllBooksPage(page_content)
for book in all_books_page.books:
    print(book)

