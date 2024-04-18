#!/usr/bin/python3
"""This module defines a python program that filters states based on a user input name
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ Check if correct number of arguments is provided"""
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
                .format(sys.argv[0]))
        sys.exit(1)

    """Extract command-line arguments"""
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    """ Connect to MySQL server"""
    conn = MySQLdb.connect(host='localhost', user=username,
                           passwd=password, db=dbname)
    cur = conn.cursor()

    """ Execute SQL query to select states based on user input"""
    stmt = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(stmt, (state_name,))

    """ Fetch and print results"""
    result = cur.fetchall()
    for row in result:
        print(row)

    """ Close database connection"""
    conn.close()
