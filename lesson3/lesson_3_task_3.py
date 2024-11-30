from address import Address  # Импортируем класс Address
from mailing import Mailing  # Импортируем класс Mailing

# Создаем экземпляры класса Address
to_address = Address("123456", "Москва", "Тверская", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Невский", "20", "15")

# Создаем экземпляр класса Mailing
mailing = Mailing(to_address, from_address, 250, "TRK123456")

# Выводим информацию об отправлении
print(f'Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.')