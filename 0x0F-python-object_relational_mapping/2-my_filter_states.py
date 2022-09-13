#!/usr/bin/python3
"""  python script that lists all states with a name starting with N """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE '{:s}' ORDER BY\
                id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
