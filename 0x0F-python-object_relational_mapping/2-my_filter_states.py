#!/usr/bin/python3

""" displays records where name matches the argument given """

import MySQLdb
import sys

if __name__ == 'main':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306)

    cursor = conn.cursor()

    sql_query = """
        SELECT * FROM states
        WHERE name = %s
        ORDER BY states.id ASC
        """

    results = cursor.execute(sql_query, (state_name)).fetchall()

    for row in results:
        print(row)

    cursor.close()
    conn.close()
