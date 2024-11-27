def is_year_leap(year):
    return year % 4 == 0

year_to_check = int(input("Введите год для проверки: "))

is_leap_year = is_year_leap(year_to_check)

print(f'Год {year_to_check}: {is_leap_year}')