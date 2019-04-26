import pyodbc
import time

QUERY = "SELECT *\nFROM sys.tables t\nJOIN sys.tables c\nON 1=1"
CONFIG = {"Driver": "{SQL Server}",
          "Server": "ggku2ser9",
          "Trusted_Connection": "no",
          "uid": "sa",
          "pwd": "Hyderabad007",
          "database": "master"
          }
TOTAL_CONNECTIONS = 3000


def check_concurrency():
    connections = []
    curs = []
    for i in range(TOTAL_CONNECTIONS):
        start = time.clock()
        # test_concurrency()
        connections.append(pyodbc.connect(**CONFIG))
        curs.append(connections[i].cursor())
        curs[i].execute(QUERY)
        rows = curs[i].fetchall()
        print(f"Connection number: {i}")
        print(f"Time taken: {time.clock() - start}")


if __name__ == '__main__':
    starttime = time.clock()
    check_concurrency()
    time.sleep(12)
    print(f"{TOTAL_CONNECTIONS} connections succeeded")
    print(f"Total time: {time.clock() - starttime}")
