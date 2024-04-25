#!/usr/bin/python3
"""
takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb


def search_state(username, password, database, stateName):
    try:
        db = MySQLdb.connect(
                host='localhost', port=3306,
                user=username, passwd=password,
                db=database
                )
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

        cursor.execute(query, (stateName,))

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


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    stateName = sys.argv[4]

    search_state(username, password, database, stateName)
