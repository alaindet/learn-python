import requests
import json
import time
from sys import argv
from pathlib import Path

from pages.all_books_page import AllBooksPage

BOOKS_URL = 'https://books.toscrape.com/catalogue/page-{}.html'
TEMP_FILE = 'books.temp.json'

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

def scrape_books_page(page_number=1) -> AllBooksPage:
    url = BOOKS_URL.format(page_number)
    page_content = requests.get(url).text
    return AllBooksPage(page_content)


def scrape_books() -> list:

    # Log
    print('Scraping...')
    start_total_time = time.time()

    # Scrape first page
    first_page = scrape_books_page(1)
    pages_count = first_page.page_count
    pages_count_padding = len(str(pages_count))

    # Scrape remaining pages on loop
    for page_number in range(2, pages_count + 1):

        start_time = time.time()
        page = scrape_books_page(page_number)
        books.extend(page.books)
        stop_time = time.time()

        # Log
        parsed_time = '%.3f' % (stop_time - start_time)
        parsed_page = str(page_number + 1).rjust(pages_count_padding, '0')
        print(f'Scraped page {parsed_page} / {pages_count} in {parsed_time} seconds')

    # Log
    stop_total_time = time.time()
    parsed_total_time = '%.3f' % (stop_total_time - start_total_time)
    print(f'Scraped {pages_count} pages in {parsed_total_time} seconds')

    return books


# Load from cache
if Path(TEMP_FILE).is_file() and not should_force:
    books = load_books_from_cache()

# Build books list
else:
    books = scrape_books()
    store_books_to_cache(books)
