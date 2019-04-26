# import csv
#
# sniffer = csv.Sniffer()
# print(sniffer.preferred)
# sniffer.preferred = [',', '\t', ';', ' ', ':', '|']
# dialect = sniffer.sniff('quarter dime  nickel | penny')
# print(dialect.delimiter)
#
# import pyodbc
# print(pyodbc.ROWID)

a = (1,2, )
b = {5: 2, a:3}
print(b)
a =(3,4)
print(b)



# Traceback (most recent call last):
# File "C:\Users\rakesh.alluri\Music\Python\CrashCourse\venv\lib\site-packages\pandas\__init_.py", line 26, in <module>
# from pandas.libs import (hashtable as hashtable,
#                          File "C:\Users\rakesh.alluri\Music\Python\CrashCourse\venv\lib\site-packages\pandas\_libs\__init_.py", line 4, in <module>
from .tslib import iNaT, NaT, Timestamp, Timedelta, OutOfBoundsDatetime
File "pandas\_libs\tslibs\conversion.pxd", line 11, in init pandas.libs.tslib
File "pandas\_libs\tslibs\conversion.pyx", line 40, in init pandas.libs.tslibs.conversion
ImportError: cannot import name parse_datetime_string
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
#                             File "C:\Users\rakesh.alluri\Music\Python\CrashCourse\venv\lib\site-packages\pandas\__init__.py", line 35, in <module>
#                                                                                                                                            "the C extensions first.".format(module))
# ImportError: C extension: parse_datetime_string not built. If you want to import pandas from the source directory, you may need to run 'python setup.py build_ext --inplace --force' to build the C extensions first.