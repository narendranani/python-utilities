import pandas as pd
import os
import pyodbc
import datetime
from sqlalchemy import create_engine, event
from sqlalchemy.pool import StaticPool

now = datetime.datetime.now()
print(now)
nowTable = "KPi_ode_dde_usage"
data = pd.read_csv("sample_writer.csv")
# data[data == 'ansi']
# data.columns = ["a"]
# print(data)
print('read data')

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ggku2ser9;'
                      'Database=Ruffalo_EDW_Temp;'
                      'Trusted_Connection=yes;')
print('Connection Successful')
cur = cnxn.cursor()

engine = create_engine("mssql+pyodbc://", poolclass=StaticPool, creator=lambda: cnxn)
# insert_query = 'INSERT INTO KPi_ode_dde_usage( type, [month], subscription, is_internal, num_user_logins, ' \
#                'potential_users, num_page_requests, avg_report_return_time, num_emailed_reports) ' \
#                'VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?) '
# # print(data.values, type(data.values))

data.to_sql(name=nowTable, con=engine, schema='dbo', index=False, if_exists='append')
# cur.executemany(insert_query, [tuple(x) for x in data.values])

cur.commit()
# for index,row in data.iterrows():
#     cur.execute("INSERT INTO "+nowTable+"([data]) values (?)", str(row['a']).encode())
#     print(index,row)
#     #now1 = datetime.datetime.now()
#     #print(now1)
#     cnxn.commit()
cur.close()
cnxn.close()
now = datetime.datetime.now()
print(now)
