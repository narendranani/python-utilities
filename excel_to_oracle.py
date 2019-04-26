import pandas as pd
from sqlalchemy import create_engine, event
from urllib.parse import quote_plus
import os
import json

BATCH = 1000


<<<<<<< HEAD
conn = "Driver={SQL Server};Server=ggku2ser9;Database=Ruffalo_EDW_Temp;Trusted_Connection=yes;"
conn = "Driver={SQL Server};SERVER=CVIADCM01;DATABASE=ConsolidatedKPIs;UID=nkommoju;PWD=Hyderabad445"
quoted = quote_plus(conn)
new_con = 'mssql+pyodbc:///?odbc_connect={}'.format(quoted)
print(new_con)
engine = create_engine(new_con)
print('Connected to DB')
df.to_sql(name='business', con=engine, schema='dbo', index=False, if_exists='replace')
=======
def load_json(path):
    with open(path) as fil:
        return json.load(fil)
>>>>>>> dc3e3e43e2399228ba1ef8a844208e723d51e407


class ExcelToOracle:
    def __init__(self, file_path, config):
        self.file_path = file_path
        conn = f'Driver={{SQL Server}};SERVER={config["Server"]};DATABASE={config["Database"]};' \
            f'UID={config["UserName"]};PWD={config["Password"]}'
        quoted = quote_plus(conn)
        self.new_con = 'mssql+pyodbc:///?odbc_connect={}'.format(quoted)
        self.table_name = config["TableName"]
        self.schema = config["Schema"]

    def excel_to_oracle(self):
        df = pd.read_excel(self.file_path)
        engine = create_engine(self.new_con)
        df.to_sql(name=self.table_name, con=engine, schema=self.schema, index=False, if_exists='append',
                  chunksize=BATCH)


if __name__ == '__main__':
    config = load_json('config.json')
    file_path = os.path.abspath(config["FilePath"])
    eto = ExcelToOracle(file_path, config)
    eto.excel_to_oracle()
    print('Successfully loaded the data to Oracle')
