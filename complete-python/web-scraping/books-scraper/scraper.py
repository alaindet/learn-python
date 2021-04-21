import requests
import json
import time
from sys import argv
from pathlib import Path

from pages.all_books_page import AllBooksPage

BOOKS_URL = 'https://books.toscrape.com/catalogue/page-{}.html'
TEMP_FILE = 'books.temp.json'
PAGES = 50

books = []
script, *options = argv
should_force = '--force' in options

def load_books_from_cache() -> list:
    with open(TEMP_FILE, 'r') as file:
        books_json = json.load(file)
        return books_json['books']

def store_books_to_cache(books) -> None:
    with open(TEMP_FILE, 'w') as file:
        json_content = {'books': books}
        json.dump(json_content, file)
        print('Books stored in temporary file')

def scrape_books() -> list:
    print('Scraping...')
    start_total_time = time.time()
    pages_padding = len(str(PAGES))

    # Scrape pages on loop
    for page_number in range(PAGES):
        start_time = time.time()
        url = BOOKS_URL.format(page_number + 1)
        page_content = requests.get(url).text
        page = AllBooksPage(page_content)

        # Parse books in page and add to list
        books.extend(page.books)
        stop_time = time.time()
        parsed_time = '%.3f' % (stop_time - start_time)
        parsed_page = str(page_number + 1).rjust(pages_padding, '0')
        print(f'Scraped page {parsed_page} / {PAGES} in {parsed_time} seconds')

    stop_total_time = time.time()
    parsed_total_time = '%.3f' % (stop_total_time - start_total_time)
    print(f'Scraped {PAGES} pages in {parsed_total_time} seconds')

    return books


if Path(TEMP_FILE).is_file() and not should_force:
    books = load_books_from_cache()
else:
    books = scrape_books()
    store_books_to_cache(books)
