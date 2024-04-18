#!/usr/bin/python3

"""
Script to list all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]

    """Establishing connection to the MySQL database"""
    db = MySQLdb.connect(port=3306, user=user, passwd=passwd, db=db_name)

    """Creating cursor for database interaction"""
    cursor = db.cursor()
    
    """SQL query to select cities with corresponding state names"""
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """

    cursor.execute(query)

    """Fetch all the rows"""
    rows = cursor.fetchall()
    for city in rows:
        print(city)

    """Closing cursor and database connection"""
    cursor.close()
    db.close()
