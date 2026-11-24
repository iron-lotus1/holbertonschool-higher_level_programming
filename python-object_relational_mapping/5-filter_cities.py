#!/usr/bin/python3
import MySQLdb
import sys


import MySQLdb
import sys


def filter_cities_by_state():
    """
    Connects to MySQL database and prints all cities
    of a given state separated by commas.
    """
    if len(sys.argv) != 5:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    cursor = db.cursor()
    query = (
        "SELECT cities.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    # Extract city names and join them with ', '
    cities_list = [row[0] for row in rows]
    print(", ".join(cities_list))

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_cities_by_state()
