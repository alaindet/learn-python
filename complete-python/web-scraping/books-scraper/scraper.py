import requests
import json
import time
import logging
from sys import argv
from pathlib import Path

from pages.all_books_page import AllBooksPage

# Logger setup
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG,
    filename='logs.temp.txt'
)
logger = logging.getLogger('scraping')

BOOKS_URL = 'https://books.toscrape.com/catalogue/page-{}.html'
TEMP_FILE = 'books.temp.json'

books = []
script, *options = argv
should_force = '--force' in options


def load_books_from_cache() -> list:
    logger.info('Loading books from cache')
    with open(TEMP_FILE, 'r') as file:
        books_json = json.load(file)
        return books_json['books']


def store_books_to_cache(books) -> None:
    logger.info('Storing books to cache')
    with open(TEMP_FILE, 'w') as file:
        json_content = {'books': books}
        json.dump(json_content, file)
        print('Books stored in temporary file')


def scrape_books_page(page_number=1) -> AllBooksPage:
    logger.info(f'Scraping book page {page_number}')
    url = BOOKS_URL.format(page_number)
    page_content = requests.get(url).text
    page = AllBooksPage(page_content)
    return page


def scrape_books() -> list:

    # Log
    logger.info('Scraping all books')
    start_total_time = time.time()

    # Scrape first page
    start_time = time.time()
    first_page = scrape_books_page(1)
    pages_count = first_page.page_count
    pages_count_padding = len(str(pages_count))
    stop_time = time.time()

    # Log
    log_time = '%.3f' % (stop_time - start_time)
    log_page = str(1).rjust(pages_count_padding, '0')
    logger.info(
        f'Scraped page {log_page} / {pages_count} in {log_time} seconds')

    # Scrape remaining pages on loop
    for page_number in range(2, pages_count + 1):

        start_time = time.time()
        page = scrape_books_page(page_number)
        books.extend([book.parse() for book in page.books])
        stop_time = time.time()

        # Log
        log_time = '%.3f' % (stop_time - start_time)
        log_page = str(page_number).rjust(pages_count_padding, '0')
        logger.info(
            f'Scraped page {log_page} / {pages_count} in {log_time} seconds')

    # Log
    stop_total_time = time.time()
    log_total_time = '%.3f' % (stop_total_time - start_total_time)
    logger.info(f'Scraped {pages_count} pages in {log_total_time} seconds')

    return books


# Load from cache
if Path(TEMP_FILE).is_file() and not should_force:
    books = load_books_from_cache()

# Build books list
else:
    books = scrape_books()
    store_books_to_cache(books)
