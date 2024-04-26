#!/usr/bin/python3
import sys
import MySQLdb


def list_states(username, password, database):
    """
    list all states from the database
    hbtn_0e_0_usa
    """

    db = MySQLdb.connect(
            host='localhost',
            port=3306, user=username,
            passwd=password, db=database)

    with db.cursor() as cursor:

        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
