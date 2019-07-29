# -*- coding: utf-8 -*-

# --------------------------------------
# Program by Andrey P.
#
#
# Version       Date        Info
# 1.0           2018        Initial Version
# 
# --------------------------------------

import sqlite3
import sys

DB_NAME = 'db.sqlite'

def deleteDB(db_name):
    '''Удаление всех записей в базе данных'''
    try:
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute('''
                    DELETE FROM contingent 
                  ''')
        conn.commit()
        c.close()
        conn.close()
    except:
        print('ERROR: ', sys.exc_info()[1])

deleteDB(DB_NAME)
