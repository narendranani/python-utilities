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
print(data)
print('read data')
data.to_csv("sample_writer_1.csv", index=False)
print(data.dtypes)
