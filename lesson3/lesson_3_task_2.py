from smartphone import Smartphone
catalog = [
    Smartphone("Apple", "iPhone 14", "+79001234567"),
    Smartphone("Samsung", "Galaxy S22", "+79007654321"),
    Smartphone("Xiaomi", "Redmi Note 11", "+79009876543"),
    Smartphone("Google", "Pixel 6", "+79003456789"),
    Smartphone("OnePlus", "9 Pro", "+79004567890")]

for smartphone in catalog:
    print(f'{smartphone.phone_brand} - {smartphone.phone_model}. {smartphone.phone_number}')