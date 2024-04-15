#!/usr/bin/python3

""" lists all states with a name starting with N from db """

import MySQLdb
import sys

if __name__ == 'main':
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
        port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT *
    FROM states
    WHERE name LIKE 'N%'
    ORDER BY states.id ASC
    """)
    results = cursor.fetchall()

    for row in results:
        # print(f'({row[0]}, \'{row[1]}\')')
        print(row)

    cursor.close()
    db.close()
