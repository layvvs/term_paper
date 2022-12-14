import sqlite3
import traceback
import sys

class Library():
    def __init__(self):
        try:
            sqlite_connection = sqlite3.connect('bpkey.db')
            cursor = sqlite_connection.cursor()
            print("База данных создана и успешно подключена к SQLite")
            cursor = sqlite_connection.cursor()
            print("База данных подключена к SQLite")
            cursor.execute('''CREATE TABLE track_info (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL UNIQUE,  
                                        bpm text NOT NULL,
                                        key text NOT NULL);''')
            sqlite_connection.commit()
            print("Таблица SQLite создана")

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)

        finally:
            if (sqlite_connection):
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")

    def add(self, name: str, bpm: str, key: str):
        try:
            sqlite_connection = sqlite3.connect('bpkey.db')
            cursor = sqlite_connection.cursor()
            print("База данных подключена к SQLite")
            cursor.execute(f"""INSERT INTO track_info
                                  (name, bpm, key)  VALUES  ('{name}', '{bpm}', '{key}')""")
            sqlite_connection.commit()
            print("Запись успешно вставлена в таблицу track_info ")
            cursor.close()

        except sqlite3.Error as error:
            print("Не удалось вставить данные в таблицу sqlite")
            print("Класс исключения: ", error.__class__)
            print("Исключение", error.args)
            print("Печать подробноcтей исключения SQLite: ")
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))

        finally:
            if (sqlite_connection):
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")

    def show(self) -> list:
        try:
            sqlite_connection = sqlite3.connect('bpkey.db')
            cursor = sqlite_connection.cursor()
            print("База данных подключена к SQLite")
            cursor.execute("""SELECT * FROM track_info""")
            sqlite_connection.commit()
            data = cursor.fetchall()
            cursor.close()

        except sqlite3.Error as error:
            print("Не удалось вывести таблицу sqlite")
            print("Класс исключения: ", error.__class__)
            print("Исключение", error.args)
            print("Печать подробноcтей исключения SQLite: ")
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))

        finally:
            if (sqlite_connection):
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")
                return data

    def remove(self, id: int):
        try:
            sqlite_connection = sqlite3.connect('bpkey.db')
            cursor = sqlite_connection.cursor()
            print("База данных подключена к SQLite")
            cursor.execute(f"""DELETE from track_info where id = {id}""")
            sqlite_connection.commit()
            print("Запись удалена")
            cursor.close()

        except sqlite3.Error as error:
            print("Не удалось удалить запись из таблицы sqlite")
            print("Класс исключения: ", error.__class__)
            print("Исключение", error.args)
            print("Печать подробноcтей исключения SQLite: ")
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))

        finally:
            if (sqlite_connection):
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")
