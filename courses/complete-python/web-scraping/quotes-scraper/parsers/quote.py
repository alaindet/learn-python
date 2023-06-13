from locators.quote_locators import QuoteLocators

class QuoteParser:
    """
    Given one of the .quote elements, find out data about the quote
    i.e. author, tags, content
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        tag_elements = self.parent.select(locator)
        return [tag_element.string for tag_element in tag_elements]