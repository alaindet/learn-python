
def readKilometers() -> float:
    while (True):
        try:
            km_input = input('> ')
            return float(km_input)
        except ValueError:
            print('Invalid input for kilometers, try again')

def convertKilometersToMiles(km: float) -> float:
    mi_to_km_factor = 1.60934
    return km * mi_to_km_factor

print('Mileage Converter')
print('How many kilometers did you travel today?')
km = readKilometers()
mi = convertKilometersToMiles(km)
print(f'{km} kilometers are equal to {mi:.2f} miles')