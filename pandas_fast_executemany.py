import pyodbc
import pandas as pd
import numpy as np
import time
from sqlalchemy import create_engine, event
from urllib.parse import quote_plus

# conn =  "DRIVER={ODBC Driver 17 for SQL Server};SERVER=IP_ADDRESS;DATABASE=DataLake;UID=USER;PWD=PASS"
conn = "Driver={SQL Server};Server=ggku2ser9;Database=Ruffalo_EDW_Temp;Trusted_Connection=yes;"
quoted = quote_plus(conn)
new_con = 'mssql+pyodbc:///?odbc_connect={}'.format(quoted)
engine = create_engine(new_con)
print('Connected to DB')

@event.listens_for(engine, 'before_cursor_execute')
def receive_before_cursor_execute(conn, cursor, statement, params, context, executemany):
    print("FUNC call")
    if executemany:
        cursor.fast_executemany = True


table_name = 'KPi_ode_dde_usage'
df = pd.read_csv("sample_writer.csv")

s = time.time()
df[:10].to_sql(table_name, engine, if_exists='append', chunksize=None, index=False)
print(time.time() - s)
