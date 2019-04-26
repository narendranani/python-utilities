import csv
import operator


def csv_sort():
    with open('wfdetails.csv', 'rb') as ifile:
        infile = csv.reader(ifile)
        # Get column header
        column_header = infile.next()
        # Get the index of 'appName' column
        appName_index = column_header.index('appName')
        # Sort(descending) the file based on the column 'appName'
        sorted_data = sorted(infile, key=operator.itemgetter(appName_index), reverse=True)

    with open('wfdetails_out.csv', 'wb') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(column_header)
        csv_writer.writerows(sorted_data)


csv_sort()
