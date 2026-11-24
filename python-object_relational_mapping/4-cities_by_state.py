#!/usr/bin/python3
"""Lists all cities with their corresponding states."""

import MySQLdb
from sys import argv


def list_cities(username, password, database):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "INNER JOIN states "
        "ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(argv) == 4:
        list_cities(argv[1], argv[2], argv[3])
