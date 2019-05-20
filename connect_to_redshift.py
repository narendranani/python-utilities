import psycopg2 as ps

conn = ps.connect(dbname= 'analyticsdb', host='nk-analytics-dev-xxxxxxxx-west-2.redshift.amazonaws.com', port= '5439', user= 'Test', password= 'xxxxxxxx')

cur = conn.cursor()
cur.execute('select top 100 * from adwords.geostats')
print("Connected successfully.")

def ResultIter(cursor, arraysize=1000):
    'An iterator that uses fetchmany to keep memory usage down'
    while True:
        results = cursor.fetchmany(arraysize)
        if not results:
            break
        for result in results:
            yield result

for result in ResultIter(cur):
    final = result

print(final)
# import numpy as np
# data = np.array(cur.fetchall())
# print(data[0])
# print("count: ", len(data))


cur.close()
