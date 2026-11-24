#!/usr/bin/python3
"""Lists all cities with their states"""

import MySQLdb
from sys import argv


def list_cities(username, password, database, state):
    db = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT name FROM cities "
        "WHERE state_id like "
        "(SELECT id FROM states WHERE name = %s)"
        " ORDER BY cities.id ASC;",
        (state,))

    rows = cursor.fetchall()

    res = ""

    for row in rows:
        res += f"{row[0]}, "

    print(res[:-2])

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities(argv[1], argv[2], argv[3], argv[4])
