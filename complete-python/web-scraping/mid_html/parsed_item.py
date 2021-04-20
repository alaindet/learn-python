from bs4 import BeautifulSoup
import re

class ParsedItem():

    locators = {
        'name': '.product_pod h3 a',
        'link': '.product_pod h3 a',
        'price': '.product_pod .product_price .price_color',
        'rating': '.product_pod .star-rating',
    }

    ratings = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
    }

    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, 'html.parser')
        self.rating_classes = self.ratings.keys()

    @property
    def name(self) -> str:
        name_element = self.soup.select_one(self.locators['name'])
        return name_element.attrs['title']


    @property
    def link(self) -> str:
        link_element = self.soup.select_one(self.locators['link'])
        return link_element.attrs['href']

    @property
    def price(self) -> float:
        price_element = self.soup.select_one(self.locators['price'])
        raw_price = price_element.string  # £123.45
        pattern = '£([0-9]+\.[0-9]{2})'
        matches = re.search(pattern, raw_price)
        return float(matches.group(1))

    @property
    def rating(self) -> int:
        rating_element = self.soup.select_one(self.locators['rating'])
        classes = rating_element.attrs['class']  # ['star-rating', 'Two']
        filtered_classes = [c for c in classes if c in self.rating_classes]
        rating_class = filtered_classes[0]
        return self.ratings[rating_class]
