#!/usr/bin/python3

""" Lists all states from database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == 'main':
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)

    cursor = db.cursor()

    query = 'SELECT * FROM states ORDER BY states.id ASC'
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(f'({row[0]}, \'{row[1]}\')')

    cursor.close()
    db.close()
