import re

print('\nExample 1')
value = 'alain.det@gmail.com'
pattern = '^[a-z\.]+\@[a-z]+\.[a-z]{1,}$'
matches = re.search(pattern, value)
print(matches.group(0))

print('\nExample 2')
value = 'Price: $123.45'
pattern = '^Price: \$([0-9]+\.[0-9]{2})$'
matches = re.search(pattern, value)
print(matches.group(0)) # Entire match
print(matches.group(1)) # First group
price = float(matches.group(1))

# Calculate the total price!
print('\nExample 3')

price_tags = (
    'Price: $111.22',
    'Some invalid price tag',
    'Price: $222.33',
    'Price: $333.44',
    'Another invalid price tag',
    'Price: $444.55',
)

def tag_to_price(tag: str) -> float:
    """
    Converts a string price tag into an actual price as a float
    If given an invalid price tag, returns 0
    """
    try:
        pattern = '^Price: \$([0-9]+\.[0-9]{2})$' # This could go out of function
        matches = re.search(pattern, tag)
        price = matches.group(1)
        return float(price)
    except:
        return 0 # If given an invalid string, price is 0

prices = [tag_to_price(price) for price in price_tags]
total = sum(prices)
print(total) # 1111.54
