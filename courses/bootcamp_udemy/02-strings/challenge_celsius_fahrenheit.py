"""
This converts temperatures from °C to °F and viceversa
"""

CELSIUS_TO_FAHRENHEIT = 'c2f'
FAHRENHEIT_TO_CELSIUS = 'f2c'

print("""
Celsius to Fahrenheit and Fahrenheit to Celsius temperature converter
- Type "c2f" for °C to °F
- Type "f2c" for °F to °C
""")

mode = input('Choose mode: ')

if mode == CELSIUS_TO_FAHRENHEIT:
    c = float(input('Enter °C: '))
    f = (9 / 5) * c + 32
    print('°F:', f)
else:
    f = float(input('Enter °F: '))
    c = (f - 32) * (5 / 9)
    print('°C:', c)

print('\nBye!')
