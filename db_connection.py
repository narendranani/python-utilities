import csv
import pyodbc
import os

CREDENTIALS = {
    'Trusted_Connection': 'no',
    'driver': '{SQL Server}',
    'server': 'ggku2ser9',
    'database': 'Ruffalo_EDW_Temp',
    'user': 'sa',
    'password': 'Hyderabad007',
    'autocommit': False,
}

BATCH = 100
cnx = pyodbc.connect(**CREDENTIALS)


def fetch_data():
    try:
        query = 'SELECT * FROM KPI_ODE_DDE_USAGE'
        cursor = cnx.cursor()
        data = cursor.execute(query)
        rows = data.fetchall()
        # rows = data.fetchone()
        # rows = data.fetchmany(2)
        print(rows)
        cursor.close()
    except Exception as error:
        print(f'Error: {error}')
        cnx.close()


def insert_data():
    try:
        query = "INSERT INTO KPI_ODE_DDE_USAGE( type, [month], subscription, is_internal, num_user_logins, " \
                "potential_users, num_page_requests, avg_report_return_time, num_emailed_reports) " \
                "VALUES( 'ODE','1/1/2017 0:00','20th Century Fox','N',3,18,49,4.85926958,0) "
        cursor = cnx.cursor()
        cursor.execute(query)
        print(cursor.rowcount)
        cursor.close()
    except Exception as error:
        print(f'Error: {error}')
        cnx.close()


fetch_data()
# insert_data()
