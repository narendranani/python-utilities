import psycopg2
import time
import os
from multiprocessing import Process
from math import ceil
import sys

# QUERY = "SELECT *\nFROM information_schema.columns t, information_schema.columns c"
QUERY = "SELECT *\nFROM information_schema.tables"
CONFIG = {"host": "deleteme.xxxxxxx.us-east-2.redshift.amazonaws.com",
          "port": "5439",
          "user": "sa",
          "password": "xxxxxxxxxxx",
          "dbname": "deletemedb"
          }
MAX_CONNECTIONS = 500
START_TIME = time.clock()
POOL = 50


def check_concurrency():
    connections = []
    curs = []
    try:
        for i in range(ceil(MAX_CONNECTIONS / POOL)):
            start = time.clock()
            connections.append(psycopg2.connect(**CONFIG))
            curs.append(connections[i].cursor())
            curs[i].execute(QUERY)
            rows = curs[i].fetchall()
            print(f"Connection number: {i}")
            print(f"Time taken: {time.clock() - start}")

    except Exception as error:
        print(f"Error: {error}")
        print(f"{MAX_CONNECTIONS} connections succeeded")
        print(f"Total time: {time.clock() - START_TIME}")
        sys.exit(0)


if __name__ == '__main__':
    procs = []
    for idx in range(POOL):
        proc = Process(target=check_concurrency, args=())
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    print(f"{MAX_CONNECTIONS} connections succeeded")
    print(f"Total time: {time.clock() - START_TIME}")
    time.sleep(10)
