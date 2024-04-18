#!/usr/bin/python3

""" Displays all values in the states table """

import MySQLdb
import sys

if __main__ == '__name__':
    db = MySQLdb.connect(
        host='locahost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
        port=3306)

    cursor = db.cursor()

    sql_query = """
    SELECT *
    FROM states
    WHERE name = {}
    ORDER BY states.id
    """, format(sys.argv[4])

    results = cursor.execute(sql_query)

    for row in results:
        print(row)

    cursor.close()
    db.close()
