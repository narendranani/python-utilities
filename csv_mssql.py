import csv
import pyodbc
import os
import time

CREDENTIALS = {
    'Trusted_Connection': 'no',
    'driver': '{SQL Server}',
    'server': 'Narendra/SQlServer',
    'database': 'Test',
    'user': 'nkommoju',
    'password': 'xxxxxxx',
    'autocommit': False,
}

BATCH = 1000

TABLE_NAME = 'KPI_Movies_Usage_deleteme'


class CsvToMssql:
    def __init__(self, file_name):
        self.in_file_name = file_name
        self.cnx = pyodbc.connect(**CREDENTIALS)
        print('Connection Established')

    def read_csv_file_generator(self):
        # try:
        with open(self.in_file_name, 'r', newline='\n', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=',')
            header = next(csv_reader)
            yield header
            while True:
                rows = (next(csv_reader, None) for x in range(BATCH))
                rows = [row for row in rows if row]
                yield rows
                if not rows:
                    return

    # except Exception as error:
    #     print(f'Error read_csv_file_generator: {error}')

    def write_to_mssql(self, data):
        try:
            self.cursor = self.cnx.cursor()
            print(data)
            # insert_query = 'INSERT INTO [KPI_Movies_Usage]( Developer, [Submitted Hours], IssueKey, ProjectName, Title_Comment_Description, ReleaseMonth, Product, [% of time], UniqueID, Contributor, Username, EmpID, [Full name], Manager, Location, Country, Confirmed, [Method Documentation], [Final Hours], Contributor2) ' \
            #                'VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '
            # self.cursor.executemany(insert_query, data)
            columns = '[Date], Product, [User_Id], Client, Internal_User, Page_View_Count'
            insert_query = self.get_insert_query(columns, data)
            self.cursor.execute(insert_query)
            print('Success')
            # self.cnx.commit()
            self.cursor.close()
        except Exception as error:
            print(f'Error write_to_mssql: {error}')
            self.cnx.rollback()
            self.cursor.close()

    def get_insert_query(self, columns, data):
        inert_query = f"insert into {TABLE_NAME}({columns}) values"
        rows = ['(' + ','.join('NULL' if not value else  "'" + value.replace("'", "''") + "'"for value in row) + ')' for
                row
                in data]
        return inert_query + ',\n'.join(rows)

    def get_insert_query(self, columns, data):
        inert_query = f"insert into {TABLE_NAME}({columns}) values"
        rows = ['(' + ','.join('NULL' if not value else  "'" + value.replace("'", "''") + "'" if isinstance(value, str) else value.replace("'", "''") for value in row) + ')' for
                row
                in data]
        return inert_query + ',\n'.join(rows)


    def close_connection(self):
        self.cnx.close()


if __name__ == '__main__':
    ctm = CsvToMssql(os.path.abspath(r'E:\D_Drive\Projects\Sheets\historical_usage.csv'))
    number = 1

    file_start = time.time()
    batch_start = time.time()

    for idx, data in enumerate(ctm.read_csv_file_generator()):
        # print(data)
        if idx == 0:
            print(f'Header: {data}')
        elif data:
            # print(data)
            # break
            ctm.write_to_mssql(data)
            # break
            batch_end = time.time()
            print(f'index: {idx} - Loaded {len(data)} rows in {round(batch_end -batch_start,2)} secs')
            # number = idx + 2
        batch_start = time.time()

    file_end = time.time()
    print(f'Loaded file in {round(file_end - file_start,2)} secs')

    ctm.close_connection()
