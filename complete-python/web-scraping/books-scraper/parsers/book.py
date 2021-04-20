from re import search

from locators.book_locators import BookLocators

class BookParser:

    ratings = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name}>'

    @property
    def name(self):
        locator = BookLocators.NAME
        element = self.parent.select_one(locator)
        return element.attrs['title']

    @property
    def link(self):
        locator = BookLocators.LINK
        element = self.parent.select_one(locator)
        return element.attrs['href']

    @property
    def price(self) -> float:
        locator = BookLocators.PRICE
        price_element = self.parent.select_one(locator)
        price_content = price_element.string # £123.45
        price_pattern = '£([0-9]+\.[0-9]{2})'
        matches = search(price_pattern, price_content)
        return float(matches.group(1))

    @property
    def rating(self) -> int:
        locator = BookLocators.RATING
        rating_element = self.parent.select_one(locator)
        classes = rating_element.attrs['class'] # ['star-rating', 'Two']
        filtered_classes = [c for c in classes if c in self.rating_classes]
        rating_class = filtered_classes[0]
        return self.ratings[rating_class]