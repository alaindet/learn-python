from bs4 import BeautifulSoup
import re

mid_html = '''
<html>
<head></head>
<body>
  <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
      <div class="image_container">
        <a href="catalogue/a-light-in-the-attic_1000/index.html">
          <img
            src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"
            alt="A Light in the Attic"
            class="thumbnail"
          >
        </a>
      </div>
      <p class="star-rating Three">
        <i class="icon-star"></i>
        <i class="icon-star"></i>
        <i class="icon-star"></i>
        <i class="icon-star"></i>
        <i class="icon-star"></i>
      </p>
      <h3>
        <a
          href="catalogue/a-light-in-the-attic_1000/index.html"
          title="A Light in the Attic"
        >
          A Light in the ...
        </a>
      </h3>
      <div class="product_price">
        <p class="price_color">£51.77</p>
        <p class="instock availability">
          <i class="icon-ok"></i>
          In stock
        </p>
        <form>
          <button
            type="submit"
            class="btn btn-primary btn-block"
            data-loading-text="Adding..."
          >
            Add to basket
          </button>
        </form>
      </div>
    </article>
  </li>
</body>
</html>
'''

soup = BeautifulSoup(mid_html, 'html.parser')

def find_item_name():
    css_locator = '.product_pod h3 a'
    item_name_element = soup.select_one(css_locator)
    name = item_name_element.attrs['title']
    print(name)

def find_item_link():
    css_locator = '.product_pod h3 a'
    item_name_element = soup.select_one(css_locator)
    link = item_name_element.attrs['href']
    print(link)

def find_item_price():
    css_locator = '.product_pod .product_price .price_color'
    item_price_element = soup.select_one(css_locator)
    raw_price = item_price_element.string # £123.45
    pattern = '£([0-9]+\.[0-9]{2})'
    matches = re.search(pattern, raw_price)
    price = float(matches.group(1))
    print(price)


def find_item_rating():
    ratings = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
    }
    rating_classes = ratings.keys()
    css_locator = '.product_pod .star-rating'
    item_rating_element = soup.select_one(css_locator)
    classes = item_rating_element.attrs['class'] # ['star-rating', 'Two']
    filtered_classes = [c for c in classes if c in rating_classes]
    rating_class = filtered_classes[0]
    rating = ratings[rating_class]
    print(rating)


find_item_name()
find_item_link()
find_item_price()
find_item_rating()
