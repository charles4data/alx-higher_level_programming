#!/usr/bin/python3

"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

db = MySQLdb.connect(
    host='localhost',
    user=sys.argv[1],
    passwd=sys.argv[2],
    database=sys.argv[3],
    port=3306)

cursor = db.cursor()

query = 'SELECT * FROM states ORDER BY states.id ASC'

results = cursor(query)

# print in this format(4, 'New York')
for row in results:
    print(f'({row[0]}, \'{row[1]}\')')

cursor.close()
db.close()
