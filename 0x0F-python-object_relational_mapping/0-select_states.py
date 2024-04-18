#!/usr/bin/python3
"""This module defines a python program that lists all states from the database
hbtn_0e_0_usa.
"""

import MySQLdb
import sys


if __name__ == '__main__':
    """
    Getting access to the database and get the states
    """
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    connect = MySQLdb.connect(host="localhost", user=username,
            passwd=password, db=dbname)
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    result = cursor.fetchall()

    for row in result:
        print(row)
