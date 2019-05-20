import pyodbc
import time

QUERY = "SELECT * FROM information_schema.tables t"
CONFIG = {"server": "{MySQL ODBC 3.51 Driver}",
          "host": "deleteme.c6z1ykk7r8lk.us-east-2.rds.amazonaws.com",
          "port": "3306",
          "user": "sa",
          "password": "xxxxxxxxxx",
          "dbname": "deletemedb"
          }
TOTAL_CONNECTIONS = 1

if __name__ == '__main__':
    starttime = time.clock()
    connections = []
    curs = []
    for i in range(TOTAL_CONNECTIONS):
        start = time.clock()
        connections.append(pyodbc.connect(**CONFIG))
        curs.append(connections[i].cursor())
        curs[i].execute(QUERY)
        rows = curs[i].fetchall()
        print("rows: ", rows)
        print(f"Connection number: {i}")
        print(f"Time taken: {time.clock() - start}")
    print(f"{TOTAL_CONNECTIONS} connections succeeded")
    print(f"Total time: {time.clock() - starttime}")
    time.sleep(60)
