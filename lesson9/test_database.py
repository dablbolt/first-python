from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://postgres:123456789m@localhost:5432/QA"
db = create_engine(db_connection_string)

def test_db_connection():
    # Используем инспектор для получения информации о таблицах
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'subject'

def test_select():
    connection = db.connect()  # Создаем соединение
    result = connection.execute(text("SELECT * FROM subject"))  # Выполняем запрос по названию указанной таблицы
    rows = result.mappings().all()  # Получаем все строки в виде словарей
    connection.close()  # Закрываем соединение

    # Проверяем, что есть хотя бы одна строка
    assert len(rows) > 0

    # Получаем первую строку
    rows1 = rows[0]

    # Проверяем значения по именам столбцов
    assert rows1["subject_id"] == 1  # Столбец называется "subject_id"
    assert rows1["subject_title"] == "English"  # Проверяем значение по имени столбца

def test_select_1_row(): # Тест на поиск по одному параметру
    connection = db.connect() # Создаем соединение
    sql_statement = text("SELECT * FROM subject WHERE subject_id = :state_id") # Запрос с параметром для фильтрации по subject_id
    result = connection.execute(sql_statement, {"state_id": 1}) # Указываем  параметр
    rows = result.mappings().all() # Получаем все строки результата в виде словарей

    assert len(rows) == 1 # Проверяем, что вернулась одна строка
    assert rows[0]["subject_title"] == "English" # Проверяем, что значение subject_title равно "English"
    connection.close() # Закрываем соединение

def test_select_1_row_with_two_filters(): # Тест на поиск по двум параметрам
    connection = db.connect()
    sql_statement = text("SELECT * FROM student WHERE \"level\" = :level_state AND user_id >= :id")    
    result = connection.execute(sql_statement, {"id": 1000, "level_state": 'Beginner'})    
    rows = result.mappings().all()

    assert len(rows) == 493
    connection.close() 

def test_insert(): # Функция вставки нового значения в таблицу student
    connection = db.connect()
    transaction = connection.begin() # Новая транзакция для выполнения операций вставки

    sql = text("INSERT INTO student(\"level\") VALUES (:new_level)")
    connection.execute(sql, {"new_level":"SkyPro"}) # Передаём значение в столбец level

    transaction.commit() # Подтверждение изменений в базе данных, завершив транзакцию
    connection.close()

def test_update(): # Функция на изменение значения в таблице student
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE student SET \"education_form\" = :update_education_form WHERE user_id = :id") 
    connection.execute(sql, {"update_education_form": 'New form', "id": 42568}) # В строке по данному id в столбце education_form теперь название New form

    transaction.commit()
    connection.close()

def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM student WHERE user_id = :id")
    connection.execute(sql, {"id": 2})

    transaction.commit()
    connection.close()
    #изменения