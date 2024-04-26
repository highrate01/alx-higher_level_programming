#!/usr/bin/python3
"""
takes in the name of a state as an argument and
lists all cities of that state, using the database
"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]
    stateName = argv[4]

    db = MySQLdb.connect(
            host='localhost', port=3306,
            user=username, passwd=password,
            db=database, charset="utf8"
            )
    cursor = db.cursor()
    query = """SELECT cities.name FROM cities JOIN states
            ON cities.state_id = states.id WHERE states.name
            = %s ORDER BY cities.id ASC"""

    cursor.execute(query, (stateName, ))
    cities = cursor.fetchall()
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    cursor.close()
    db.close()
