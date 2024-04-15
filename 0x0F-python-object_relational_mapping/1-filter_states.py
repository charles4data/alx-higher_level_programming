#!/usr/bin/python3

"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

""" connect to db """
db = MySQLdb.connect(
    host='localhost',
    user=sys.argv[1],
    passwd=sys.argv[2],
    database=sys.argv[3],
    port=3306)

""" query database """
cursor = db.cursor()
query = 'SELECT * FROM states ORDER BY states.id ASC'
cursor.execute(query)
results = cursor.fetchall()

""" display results """
for row in results:
    print(f'({row[0]}, \'{row[1]}\')')

""" close database """
cursor.close()
db.close()
