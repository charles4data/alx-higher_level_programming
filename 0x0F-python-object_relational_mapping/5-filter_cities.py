#!/usr/bin/python3
""" lists all the cities of a state """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)

    cursor = db.cursor()

    sql_query = """
        SELECT cities.name
        FROM cities
        INNER JOIN states ON states.id=cities.states_id
        WHERE states.name=%s"""

    cursor.execute(sql_query, (sys.argv[4],))

    results = cursor.fetchall()

    items = list(results[0] for row in results)

    print(*items, sep=", ")

    cursor.close()
    db.close()
