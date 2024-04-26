#!/usr/bin/python3
"""
list states and save from sql injection
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    stateName = argv[4]

    db = MySQLdb.connect(
            host='localhost', port=3306, user=username,
            passwd=password, db=database, charset="utf8"
            )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    cursor.execute(query, (stateName, ))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
