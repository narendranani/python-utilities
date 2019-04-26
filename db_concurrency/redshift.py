import psycopg2
import time

QUERY = "SELECT *\nFROM information_schema.tables t"
CONFIG = {"host": "deleteme.cwl2lo84oinp.us-east-2.redshift.amazonaws.com",
          "port": "5439",
          "user": "sa",
          "password": "Hyderabad007",
          "dbname": "deletemedb"
          }
TOTAL_CONNECTIONS = 510


def check_concurrency():
    connections = []
    curs = []
    for i in range(TOTAL_CONNECTIONS):
        start = time.clock()
        connections.append(psycopg2.connect(**CONFIG))
        curs.append(connections[i].cursor())
        curs[i].execute(QUERY)
        rows = curs[i].fetchall()
        print(f"Connection number: {i}")
        print(f"Time taken: {time.clock() - start}")


if __name__ == '__main__':
    starttime = time.clock()
    check_concurrency()
    print(f"{TOTAL_CONNECTIONS} connections succeeded")
    print(f"Total time: {time.clock() - starttime}")
    # time.sleep(60)
