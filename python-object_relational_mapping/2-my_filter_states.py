#!/usr/bin/python3
"""Displays states matching a name provided by the user."""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    cur.execute(query.format(sys.argv[4]))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
