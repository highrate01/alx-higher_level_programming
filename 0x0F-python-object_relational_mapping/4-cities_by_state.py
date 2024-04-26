#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(
            host='localhost', port=3306,
            user=username, passwd=password,
            db=database, charset="utf8"
            )
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities " \
            "JOIN states ON cities.state_id = states.id " \
            "ORDER BY cities.id ASC"
    cursor.execute(query)

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
