#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


def list_Nstates(username, password, database):
    db = MySQLdb.connect(
            host='localhost', port=3306,
            user=username, passwd=password,
            db=database
            )
    cursor = db.cursor()
    try:
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)

        states = cursor.fetchall()
        for state in states:
            print(state)
    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_Nstates(username, password, database)
