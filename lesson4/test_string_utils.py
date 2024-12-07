import pytest

from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


# Тесты для метода capitalize
def test_capitilize(string_utils):
    # Позитивные тесты
    assert string_utils.capitilize("skypro") == "Skypro"  # Обычный текст
    assert string_utils.capitilize("hello") == "Hello"  # Обычный текст
    assert string_utils.capitilize("123abc") == "123abc"  # Числа в начале

    # Негативные тесты
    assert string_utils.capitilize("") == ""  # Пустая строка
    assert string_utils.capitilize(" ") == " "  # Строка с пробелом


# Тесты для метода trim
def test_trim(string_utils):
    # Позитивные тесты
    assert string_utils.trim("   skypro") == "skypro"  # Удаление пробелов в начале
    assert string_utils.trim("hello   ") == "hello   "  # Пробелы в конце не удаляются
    assert string_utils.trim("   hello   ") == "hello   "  # Пробелы с обеих сторон

    # Негативные тесты
    assert string_utils.trim("") == ""  # Пустая строка
    assert string_utils.trim(" ") == ""  # Строка с пробелом


# Тесты для метода to_list
def test_to_list(string_utils):
    # Позитивные тесты
    assert string_utils.to_list("a,b,c,d") == [
        "a",
        "b",
        "c",
        "d",
    ]  # Запятая как разделитель
    assert string_utils.to_list("1:2:3", ":") == [
        "1",
        "2",
        "3",
    ]  # Двоеточие как разделитель
    assert string_utils.to_list("04 апреля 2023", " ") == [
        "04",
        "апреля",
        "2023",
    ]  # Пробел как разделитель

    # Негативные тесты
    assert string_utils.to_list("") == []  # Пустая строка
    assert string_utils.to_list("a b c", " ") == [
        "a",
        "b",
        "c",
    ]  # Пробел как разделитель
    assert string_utils.to_list("a,b,c,d", ";") == ["a,b,c,d"]  # Неверный разделитель


# Тесты для метода contains
def test_contains(string_utils):
    # Позитивные тесты
    assert string_utils.contains("SkyPro", "S") is True  # Содержит символ
    assert string_utils.contains("SkyPro", "U") is False  # Не содержит символ
    assert string_utils.contains("Hello World", " ") is True  # Содержит пробел

    # Негативные тесты
    assert string_utils.contains("", "S") is False  # Пустая строка
    assert string_utils.contains(" ", " ") is True  # Строка с пробелом


# Тесты для метода delete_symbol
def test_delete_symbol(string_utils):
    # Позитивные тесты
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"  # Удаление символа
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"  # Удаление подстроки
    assert string_utils.delete_symbol("Hello", "l") == "Heo"  # Удаление символа

    # Негативные тесты
    assert string_utils.delete_symbol("", "k") == ""  # Пустая строка
    assert string_utils.delete_symbol(" ", " ") == ""  # Строка с пробелом
    assert string_utils.delete_symbol("Hello", "x") == "Hello"  # Символ не найден


# Тесты для метода starts_with
def test_starts_with(string_utils):
    # Позитивные тесты
    assert string_utils.starts_with("SkyPro", "S") is True  # Начинается с символа
    assert string_utils.starts_with("SkyPro", "P") is False  # Не начинается с символа

    # Негативные тесты
    assert string_utils.starts_with("", "S") is False  # Пустая строка
    assert string_utils.starts_with(" ", " ") is True  # Строка с пробелом


# Тесты для метода ends_with
def test_end_with(string_utils):
    # Позитивные тесты
    assert string_utils.end_with("SkyPro", "o") is True  # Заканчивается на символ
    assert string_utils.end_with("SkyPro", "y") is False  # Не заканчивается на символ

    # Негативные тесты
    assert string_utils.end_with("", "o") is False  # Пустая строка
    assert string_utils.end_with(" ", " ") is True  # Строка с пробелом


# Тесты для метода is_empty
def test_is_empty(string_utils):
    # Позитивные тесты
    assert string_utils.is_empty("") is True  # Пустая строка
    assert string_utils.is_empty(" ") is True  # Строка с пробелом

    # Негативные тесты
    assert string_utils.is_empty("SkyPro") is False  # Непустая строка
    assert string_utils.is_empty("  Hello  ") is False  # Строка с пробелами


# Тесты для метода list_to_string
def test_list_to_string(string_utils):
    # Позитивные тесты
    assert (
        string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    )  # Преобразование списка в строку
    assert (
        string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    )  # Преобразование списка в строку
    assert (
        string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
    )  # Разделитель '-'

    # Негативные тесты
    assert string_utils.list_to_string([]) == ""  # Пустой список
