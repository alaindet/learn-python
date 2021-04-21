import requests
import json
import time

from pages.all_books_page import AllBooksPage

BOOKS_URL = 'https://books.toscrape.com/catalogue/page-{}.html'
TEMP_FILE = 'books.temp.json'
PAGES = 50
books = []

try:

    # Load from cache
    with open(TEMP_FILE, 'r') as file:
        books_json = json.load(file)
        books = books_json['books']
        print(len(books))
        print(books[0]['name'])

except FileNotFoundError:

    print('Scraping...')
    pages_padding = len(str(PAGES))

    # Scrape pages on loop
    for page_number in range(PAGES):
        start_time = time.time()
        url = BOOKS_URL.format(page_number + 1)
        page_content = requests.get(url).text
        page = AllBooksPage(page_content)

        # Parse books in page and add to list
        page_books = page.books
        for book in page_books:
            books.append(book.parse())
        stop_time = time.time()
        parsed_time = '%.3f' % (stop_time - start_time)
        parsed_page = str(page_number + 1).rjust(pages_padding, '0')
        print(f'Scraped page {parsed_page} / {PAGES} in {parsed_time} seconds')

    # Store parsed book in temporary file for further analysis
    with open(TEMP_FILE, 'w') as file:
        json_content = {'books': books}
        json.dump(json_content, file)
