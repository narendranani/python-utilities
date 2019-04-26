import re

import pandas as pd

file_name = r'E:\BitBucket_Knarendra1154\utilities\Book1.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
# data = pd.DataFrame(columns=df.head())
# print(df.header())
data = pd.DataFrame()
df['address'] = [re.sub(r'[\w\.-]+@[\w\.-]+', "", value) for value in df['address']]
print(df)
# print(df['address'])
# for idx, row in df.iterrows():
#     print(row)
#     data.append(row)
#     # row['name'] = re.sub(r'[\w\.-]+@[\w\.-]+', "", row['name'])
#     # print(row['name'] )
# #
# # for idx, row in df.iterrows():
# #     print(row['name'] )
#
#
# print(data)