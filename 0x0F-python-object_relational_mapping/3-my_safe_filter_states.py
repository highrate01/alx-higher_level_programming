#!/usr/bin/python3
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    stateName = sys.argv[4]

    db = MySQLdb.connect(
            host='localhost', port=3306, user=username,
            passwd=password, db=database, charset="utf8"
            )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    cursor.execute(query, (stateName,))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
