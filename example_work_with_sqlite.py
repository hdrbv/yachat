import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('./db.sqlite3')

# Создание курсора
cursor = conn.cursor()

# Выполнение запроса для получения всех таблиц
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Извлечение результатов
tables = cursor.fetchall()

# Вывод списка таблиц
for table in tables:
    print(table[0])

# Выполнение SQL-запроса
cursor.execute("SELECT * FROM table")

# Извлечение всех строк результата
rows = cursor.fetchall()

# Обработка результатов
for row in rows:
    print(row)

# Закрытие курсора и соединения
cursor.close()
conn.close()



