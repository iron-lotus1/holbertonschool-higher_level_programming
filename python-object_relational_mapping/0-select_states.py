#!/usr/bin/env python3
"""Lists all states from a MySQL database."""

import MySQLdb
import sys

if __name__ == "main":
    db = MySQLdb.connect(
host="localhost",
port=3306,
user=sys.argv[1],
passwd=sys.argv[2],
db=sys.argv[3]
)
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
query_rows = cur.fetchall()

for row in query_rows:
    print(row)

cur.close()
db.close()
