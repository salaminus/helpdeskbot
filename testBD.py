import sqlite3
import sys


def queryDB(query):
    # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
    try:
        conn = sqlite3.connect('db.sqlite')
        c = conn.cursor()
        c.execute('''SELECT * 
            FROM contingent 
            WHERE fio LIKE '%s'
        ''' % (query))
        # Получаем результат сделанного запроса
        results = c.fetchall()
        print(results)   # выдается список с кортежами
    except:
        print(sys.exc_info()[1])


queryDB('Б'+'%')