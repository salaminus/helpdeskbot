import sqlite3
import sys


def queryDB(query):
    # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
    try:
        conn = sqlite3.connect('/home/salaminus/myapp/db.sqlite')
        c = conn.cursor()
        c.execute('''SELECT fio, status 
            FROM contingent 
            WHERE fio LIKE '%s'
        ''' % (query + '%'))
        # Получаем результат сделанного запроса
        data = c.fetchall()
        c.execute('''SELECT imageLink 
                    FROM contingent 
                    WHERE fio LIKE '%s'
                ''' % (query + '%'))
        # Получаем результат сделанного запроса
        imageLink = c.fetchall()
        # print(data)   # выдается список с кортежами
        return (data, imageLink)
    except:
        print(sys.exc_info()[1])

