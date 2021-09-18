import sys

import mysql.connector
from mysql.connector import Error
from pymemcache.client import base

try:
    connection = mysql.connector.connect(host='localhost', database='sakila', user='root', password='dev')
    memc = base.Client(('localhost', 11211))
    cursor = connection.cursor()
    cursor.execute("""
                SELECT COUNT(fa.actor_id), fa.actor_id, CONCAT(a.last_name, ' ', a.first_name) as full_name
                FROM film_actor as fa
                LEFT JOIN actor a on a.actor_id = fa.actor_id
                GROUP BY fa.actor_id
                ORDER BY COUNT(fa.actor_id) desc;
            """)
    rows = cursor.fetchall()
    for [count, actor_id, actor_name] in rows:
        memc.set(str(actor_id), str(actor_name))
        print(f'Record {actor_id}:{actor_name}')
except Error as e:
    print("Error reading data from MySQL table", e)
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
