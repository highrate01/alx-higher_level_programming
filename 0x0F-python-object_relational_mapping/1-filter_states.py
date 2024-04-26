#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
            host='localhost', port=3306,
            user=username, passwd=password,
            db=database, charset="utf8"
            )
    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    states = cursor.fetchall()
    for state in states:
        if state[1].startswith("N"):
            print(state)
    cursor.close()
    db.close()
