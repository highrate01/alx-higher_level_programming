#!/usr/bin/python3
"""
list all states from the database hbtn_0e_0_usai.
"""
import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

db = MySQLdb.connect(
        host='localhost',
        port=3306, user=username,
        passwd=password, db=database, charset="utf8")

with db.cursor() as cursor:

    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)
cursor.close()
db.close()
