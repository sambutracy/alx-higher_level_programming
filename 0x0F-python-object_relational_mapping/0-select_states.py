#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extracting arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL server running on localhost at port 3306
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Execute SQL query to select all states from the states table
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows using fetchall() method
        states = cursor.fetchall()

        # Print the results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
    finally:
        # Close the database connection
        if 'db' in locals() or 'db' in globals():
            db.close()
