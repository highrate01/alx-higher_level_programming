#!/usr/bin/python3
import sys
import MySQLdb
"""lists all states from the database hbtn_0e_0_usa"""


def list_states(username, password, database):

    try:
        db = MySQLdb.connect(
                host='localhost',
                port=3306, user=username,
                passwd=password, db=database
                )

        cursor = db.cursor()
        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error accessing database: {e}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db' in locals() and db:
            db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
