import csv
import pyodbc
import os
import time


CREDENTIALS = {
    'Trusted_Connection': 'no',
    'driver': '{SQL Server}',
    'server': 'CVIADCM01',
    'database': 'Jira',
    'user': 'nkommoju',
    'password': 'Hyderabad445',
    'autocommit': False,
}

BATCH = 1000


def to_csv():
    try:
        cnx = pyodbc.connect(**CREDENTIALS)
        cursor = cnx.cursor()
        select_query = "select * from [dbo].[ProductIssueWorklog]"
        print("I am here")
        cursor.execute(select_query)
        with open('ProductIssueWorklog.csv', 'w', newline='\n', encoding='utf-8') as f:
            while True:
                data = cursor.fetchmany(BATCH)
                if not data:
                    break
                csv_writer = csv.writer(f)
                csv_writer.writerows(data)
        cnx.commit()
        cursor.close()
        print('Success')
    except Exception as error:
        print(f'Error write_to_mssql: {error}')
        cnx.rollback()
        cursor.close()


def restService():
    pass


rest_Serve = 10

if __name__ == '__main__':
    to_csv()
