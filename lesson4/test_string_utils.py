import pytest

from string_utils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

# Позитивные тесты для метода capitalize
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),  # Обычный текст
    ("hello", "Hello"),    # Обычный текст
    ("123abc", "123abc"),  # Числа в начале
])
def test_capitalize_positive_case(string_utils, input_str, expected):
    assert string_utils.capitilize(input_str) == expected

# Негативные тесты для метода capitalize
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),               # Пустая строка
    (" ", " ")              # Строка с пробелом
])
def test_capitalize_negative_case(string_utils, input_str, expected):
    assert string_utils.capitilize(input_str) == expected

# Позитивные тесты для метода trim
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),      # Удаление пробелов в начале
    ("hello   ", "hello   "),      # Пробелы в конце не удаляются
    ("   hello   ", "hello   "),   # Пробелы с обеих сторон
])
def test_trim_positive_case(string_utils, input_str, expected):
    assert string_utils.trim(input_str) == expected

# Негативные тесты для метода trim
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                        # Пустая строка
    (" ", " ")                       # Строка с пробелом
])
def test_trim_negative_case(string_utils, input_str, expected):
    assert string_utils.trim(input_str) == expected

# Позитивные тесты для метода to_list
@pytest.mark.parametrize("input_str, delimiter, expected", [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),  # Запятая как разделитель
    ("1:2:3", ":", ["1", "2", "3"]),          # Двоеточие как разделитель
    ("04 апреля 2023", " ", ["04", "апреля", "2023"]),  # Пробел как разделитель
])
def test_to_list_positive_case(string_utils, input_str, delimiter, expected):
    assert string_utils.to_list(input_str, delimiter) == expected

# Негативные тесты для метода to_list
@pytest.mark.parametrize("input_str, delimiter, expected", [
    ("", "", []),                              # Пустая строка
    ("a b c", " ", ["a", "b", "c"]),         # Пробел как разделитель
    ("a,b,c,d", ";", ["a,b,c,d"])            # Неверный разделитель
])
def test_to_list_negative_case(string_utils, input_str, delimiter, expected):
    assert string_utils.to_list(input_str, delimiter) == expected

# Позитивные тесты для метода contains
@pytest.mark.parametrize("input_str, char, expected", [
    ("SkyPro", "S", True),          # Содержит символ
    ("Hello World", " ", True),     # Содержит пробел
])
def test_contains_positive_case(string_utils, input_str, char, expected):
    assert string_utils.contains(input_str, char) is expected

# Негативные тесты для метода contains
@pytest.mark.parametrize("input_str, char, expected", [
    ("SkyPro", "U", False),         # Не содержит символ
    ("", "S", False),                # Пустая строка
    (" ", " ", True)                 # Строка с пробелом
])
def test_contains_negative_case(string_utils, input_str, char, expected):
    assert string_utils.contains(input_str, char) is expected

# Позитивные тесты для метода delete_symbol
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),        # Удаление символа
    ("SkyPro", "Pro", "Sky"),        # Удаление подстроки
])
def test_delete_symbol_positive_case(string_utils, input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

# Негативные тесты для метода delete_symbol
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Hello", "l", "Heo"),           # Удаление символа
    ("", "k", ""),                    # Пустая строка
    (" ", " ", "")                    # Строка с пробелом
])
def test_delete_symbol_negative_case(string_utils, input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

# Позитивные тесты для метода starts_with
@pytest.mark.parametrize("input_str, char, expected", [
    ("SkyPro", "S", True),          # Начинается с символа
])
def test_starts_with_positive_case(string_utils, input_str, char, expected):
    assert string_utils.starts_with(input_str, char) is expected

# Негативные тесты для метода starts_with
@pytest.mark.parametrize("input_str, char, expected", [
    ("SkyPro", "P", False),         # Не начинается с символа
    ("", "S", False),                # Пустая строка
    (" ", " ", True)                 # Строка с пробелом
])
def test_starts_with_negative_case(string_utils, input_str, char, expected):
    assert string_utils.starts_with(input_str, char) is expected

# Позитивные тесты для метода ends_with
@pytest.mark.parametrize("input_str, char, expected", [
    ("SkyPro", "o", True),          # Заканчивается на символ
])
def test_end_with_positive_case(string_utils, input_str, char, expected):
    assert string_utils.end_with(input_str, char) is expected

# Негативные тесты для метода ends_with
@pytest.mark.parametrize("input_str, char, expected", [
    ("SkyPro", "y", False),         # Не заканчивается на символ
    ("", "o", False),                # Пустая строка
    (" ", " ", True)                 # Строка с пробелом
])
def test_end_with_negative_case(string_utils, input_str, char, expected):
    assert string_utils.end_with(input_str, char) is expected

# Позитивные тесты для метода is_empty
@pytest.mark.parametrize("input_str, expected", [
    ("", True),                      # Пустая строка
])
def test_is_empty_positive_case(string_utils, input_str, expected):
    assert string_utils.is_empty(input_str) is expected

# Негативные тесты для метода is_empty
@pytest.mark.parametrize("input_str, expected", [
    (" ", True)                     # Строка с пробелом
])
def test_is_empty_negative_case(string_utils, input_str, expected):
    assert string_utils.is_empty(input_str) is expected