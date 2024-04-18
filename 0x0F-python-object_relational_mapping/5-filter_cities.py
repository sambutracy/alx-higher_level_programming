#!/usr/bin/python3

"""
a script that takes in the name of a state as an
argument and lists all cities of that state
using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    """Connect to MySQL server"""
    conn = MySQLdb.connect(port=3306, user=user, passwd=passwd, db=db_name)

    """Create cursor for database interaction"""
    cursor = conn.cursor()
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))

    """Fetch all the rows"""
    rows = cursor.fetchall()

    """Print the cities"""
    cities = ', '.join(city[0] for city in rows)
    print(cities)

    """Close the cursor and database connection"""
    cursor.close()
    conn.close()
