import csv
import pyodbc

CREDENTIALS = {
    'Trusted_Connection': 'no',
    'driver': '{SQL Server}',
    'server': 'CVIADCM01',
    'database': 'consolidatedkpis',
    'user': 'nkommoju',
    'password': 'Hyderabad445',
    'autocommit': False,
}


def get_from_csv(in_file_name):
    with open(in_file_name, 'r', newline='\n', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=',')
        header = next(csv_reader)
        ids = [value[0] if value else '' for value in csv_reader]
    return set(ids)


def get_from_db():
    try:
        cnx = pyodbc.connect(**CREDENTIALS)
        cursor = cnx.cursor()
        select_query = "SELECT DISTINCT ACCOUNT_ID FROM LU_Client_Account"
        cursor.execute(select_query)
        ids = [value[0].lower() for value in cursor.fetchall()]
    finally:
        cursor.close()
        cnx.close()
    return set(ids)


def diff_check():
    status = True
    csv_ids = get_from_csv('account_id.csv')
    # print(csv_ids)
    db_ids = get_from_db()
    # print(db_ids)
    print(f'csv-db: {csv_ids - db_ids}')
    print(f'db-csv: {db_ids - csv_ids}')
    return status


if __name__ == '__main__':
    if diff_check():
        print('Success')
    else:
        print('Fail')
