#!/usr/bin/python3
""" lists all cities from database hbtn_0e_4_usa """
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
    SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states ON states.id = cities.states_id
    ORDER BY cities.id ASC
    """

    results = cursor.execute(sql_query)

    for row in results:
        print(row)

    cursor.close()
    db.close()
