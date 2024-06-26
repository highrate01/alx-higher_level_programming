#!/usr/bin/python3
"""
takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]
    stateName = argv[4]
    try:
        db = MySQLdb.connect(
                            host='localhost', port=3306,
                            user=username, passwd=password,
                            db=database, charset="utf8"
                            )
        cursor = db.cursor()

        query = """
        SELECT * FROM states WHERE name LIKE BINARY '{}'
        ORDER BY states.id ASC"""
        query = query.format(stateName)

        cursor.execute(query)

        states = cursor.fetchall()
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db' in locals() and db:
            db.close()
