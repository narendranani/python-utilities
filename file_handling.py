# """
# Text Files
# """
# # Importing modules from  a import b pip install
import os
import csv


#
#
# # Method1
# def read_txt_file(file_name):
#     file = open(file_name, 'r')
#     content = file.read()
#     print(content)
#     file.close()
#     file = open(file_name, 'r')
#     content = file.readlines()
#     for row in content:
#         print(row)
#     file.close()
#
#
# file_name = os.path.abspath('sample_read.txt')
# read_txt_file(file_name)
#
# # Method2 - Error handling
# try:
#     print(5 / 0)
# except Exception as error:
#     print(error)
#     # print(5/0)
# finally:
#     print("Finally")
#
#
# def read_txt_file(file_name):
#     try:
#         file = open(file_name, 'r')
#         content = file.read()
#         print(content)
#         # file = open(file_name, 'r')
#         # content = file.readline()
#         # print(content)
#         # file = open(file_name, 'r')
#         # content = file.readlines()
#         # print(content)
#     except Exception as error:
#         print(error)
#         # Send error notification
#     finally:
#         file.close()
#
#
# file_name = os.path.abspath('sample_read.txt')
# read_txt_file(file_name)
#
#
# # Method3 - Using Context Manager
# def read_txt_file(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             content = file.read()
#             print(content)
#     except Exception as error:
#         print(error)
#         # Send error notification
#
#
# file_name = os.path.abspath('sample_read.txt')
# read_txt_file(file_name)
#
#
# # Write to txt file
# def write_txt_file(file_name):
#     try:
#         with open('sample_read.txt', 'r') as in_file:
#             # data = in_file.read()
#             data = in_file.readlines()
#         with open(file_name, 'w') as out_file:
#             # out_file.write(data)
#             out_file.writelines(data[:2])
#         # out_file.writelines(data)
#         print('Completed writing to the file')
#     except Exception as error:
#         print(error)
#         # Send error notification
#
#
# file_name = os.path.abspath('sample_write.txt')
# write_txt_file(file_name)
#
#
# """
# # "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# # "w" - Write - Opens a file for writing, creates the file if it does not exist
# # "a" - Append - Opens a file for appending, creates the file if it does not exist
# # rb - Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file..
# # r+ - Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
# # rb+ - Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.
# # wb - Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
# # w+ - Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
# # wb+ - Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
# # ab - Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
# # a+ - Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
# # ab+ - Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
# """
#
# """
# CSV
# """
#
#
# # With & Without Encoding encoding='utf-8' â€
# # Default encoding is platform dependant -> In windows it is ANSI. But you pass the encoding
# # When ASCII was created, it only used 7 bits for a total maximum combination of 128 characters
# # In ANSI, 8 bits are used; increasing the maximum number of characters to be represented up to 256
# def read_txt_file(file_name):
#     try:
#         with open(file_name, 'r', newline='\n', encoding='utf-8') as file:
#             csv_reader = csv.reader(file, delimiter=',')
#             for row in csv_reader:
#                 print(row)
#         # Can not use the reader object after closing the file. We need
#         # for row in csv_reader:
#         #     print(row)
#     except Exception as error:
#         print(error)
#         # Send error notification
#
#
# file_name = os.path.abspath('sample_read.csv')
# read_txt_file(file_name)
#
#
# Write CSV
def write_txt_file(in_file_name, out_file_name):
    try:
        with open(in_file_name, 'r', newline='\n', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=',')
            data = [row for row in csv_reader]
        with open(out_file_name, 'a', newline='\n', encoding='utf-8') as file:
            csv_writer = csv.writer(file, delimiter=',')
            csv_writer.writerows(data)
        print('Success')
    except Exception as error:
        print(f'Error: {error}')
        # Send error notification


in_file_name = os.path.abspath('sample_read.csv')
out_file_name = os.path.abspath('sample_writer.csv')
write_txt_file(out_file_name, out_file_name)



# Handle huge data files
# import csv
#
# BATCH = 20

# generators
# nums = (a for a in range(10))
# print(next(nums))
# for i in nums:
#     print(i)
#
#
# def generator():
#     for a in range(10):
#         yield a
#
#
# for i in generator():
#     print(i)

# # Handle huge data files
# def read_csv_file_generator(in_file_name):
#     try:
#         with open(in_file_name, 'r', newline='\n', encoding='utf-8') as file:
#             csv_reader = csv.reader(file, delimiter=',')
#             header = next(csv_reader)
#             yield header
#             while True:
#                 rows = [next(csv_reader) for x in range(BATCH)]
#                 yield rows
#                 if not rows:
#                     return
#     except Exception as error:
#         print(f'Error: {error}')
#
#
# in_file_name = os.path.abspath('sample_read.csv')
# out_file_name = os.path.abspath('sample_writer.csv')
# for idx, data in enumerate(read_csv_file_generator(in_file_name, BATCH)):
#     if idx == 0:
#         print(f'Header: {data}')
#     else:
#         print(f'data: {data}')
#     # if idx == 5:
#     #     break
