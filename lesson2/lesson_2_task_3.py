import math

def square(side):  # сторона квадрата
    area = side * side  # вычислим площадь
    return math.ceil(area)  # округление

side_length = float(input("Введите длину стороны квадрата: "))

area_result = square(side_length)

print(f'Площадь квадрата со стороной {side_length}: {area_result}')