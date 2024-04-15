#!/usr/bin/python3
""" Lists all states from database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == 'main':
    """ connects to and queries a database """
    # connect to database
    db = MySQLdb.connect(
        host='localhost',
        user = sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)

    # create a cursor object
    cursor = db.cursor

    # query database
    query = 'SELECT id, name FROM states ORDER BY states.id ASC'
    cursor.execute(query)
    results = cursor.fetchall()

    # display results
    for row in results:
        print(row)

    # close connection and cursor
    cursor.close()
    db.close()
