import csv
import operator
from random import shuffle

no_of_times = 2000


def append_files():
    with open('MOCK_DATA.csv', 'r') as in_file:
        csv_reader = csv.reader(in_file, delimiter=',')
        in_rows = list(csv_reader)
        shuffle(in_rows)
    for i in range(no_of_times):
        with open('TaskUS_2Million_Records.csv', 'a', newline='\n') as out_file:
            csv_writer = csv.writer(out_file, lineterminator='\n')
            csv_writer.writerows(in_rows)
        print(f"Write csv file {i} time")


append_files()
