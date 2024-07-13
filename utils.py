import sqlite3
import csv


def delete_record():
    try:
        sqlite_connection = sqlite3.connect('db.sqlite3')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_delete_query = """DELETE from main_protocol"""
        cursor.execute(sql_delete_query)
        sqlite_connection.commit()
        print("Запись успешно удалена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def insert_to_db():
    sqlite_connection = sqlite3.connect('db.sqlite3')
    cursor = sqlite_connection.cursor()
    with open('./media/data.csv', newline='', encoding='UTF-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if len(row) == 5 and row[0] != 'Дата':
                print(row)
                sql_insert_query = """INSERT INTO main_protocol (date, time, traffic, user_id, websystem_id)
                 VALUES(?, ?, ?, ?, ?)"""
                cursor.execute(sql_insert_query, row)
                sqlite_connection.commit()

