'''
CRUD TEST REVIEW
'''

from datetime import datetime
from sqlite3 import connect
import pymysql.cursors
from contextlib import contextmanager

now = str(datetime.now())
date_now = str(now.split(' ')[0])


#TODO: use With to open and close db connections
#TODO: change this operations API to a different module
class OperateMydb:
    def connect(self):
        print('connecting...')
        self.connection = pymysql.connect(
            host = '127.0.0.1',
            user = 'root',
            password = '',
            db = 'mydb',
            charset = 'utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
        )
    
    def disconnect(self):
        print('closing connection...')
        self.connection.close()

    def insert_custommer(self):
        self.connect()
        with self.connection.cursor() as cursor:
            name = input('place a name:> ')
            address = input('place an address:> ')
            phone1 = input('place an phone:> ')

            cursor.execute('INSERT INTO custommer (name, address, client_since, phone_1) \
                VALUES (%s, %s, %s, %s)', (name, address, date_now, phone1))

        self.disconnect()

    def print_from_table(self):

        self.cursor.execute('SELECT * FROM custommer')
        result = self.cursor.fetchall()
        print(result)

        self.cursor.close()
        self.connection.close()

ops1 = OperateMydb()
ops1.insert_custommer()
# ops1.print_from_table()