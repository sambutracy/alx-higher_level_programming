#!/usr/bin/python3
"""This module defines a python program that lists states with names starting
with 'N' from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extracting command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Connect to MySQL server
    conn = MySQLdb.connect(host='localhost', user=username,
                           passwd=password, db=dbname)
    cur = conn.cursor()

    # Execute SQL query to select states starting with 'N'
    stmt = ("SELECT * FROM states WHERE name LIKE " +
            "'N%' COLLATE utf8mb4_bin ORDER BY id ASC")
    cur.execute(stmt)

    # Fetch and print results
    result = cur.fetchall()
    for row in result:
        print(row)
