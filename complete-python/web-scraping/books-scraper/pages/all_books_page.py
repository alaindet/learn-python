from bs4 import BeautifulSoup
from re import search

from locators.all_books_page import AllBooksPageLocators
from parsers.book import BookParser

class AllBooksPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')
    
    @property
    def books(self):
        book_elements = self.soup.select(AllBooksPageLocators.BOOKS)
        return [BookParser(book_element) for book_element in book_elements]

    @property
    def page_count(self):
        pager_content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matches = search(pattern, pager_content)
        pages = int(matches.group(1))
        return pages
