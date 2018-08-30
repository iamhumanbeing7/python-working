import os
from xlrd import open_workbook
from MBCCS_File_Processing import config
import re
#
# path_2016 = config.path_2016
# files_2016 = os.listdir(path_2016)
# file_2016 = files_2016[0]
# file_2016_path = os.path.join(path_2016, file_2016)
# print(file_2016)
# excelbook = open_workbook(file_2016_path)
# for sheetname in excelbook.sheet_names():
#     excelsheet = excelbook.sheet_by_name(sheetname)
#     print("worksheet name is: {0}, # of rows is: {1} ".format(excelsheet.name, excelsheet.nrows))
# if 'A' in ["C", 'B', "A"]:
#     print('A is in it!')
# print('A' in ['C', 'B', 'A'])
# print("A" == 'A')
# print('aaaaaaaabbbbbbccccc'.upper())


if re.match('\d{4}/\d{4}', '0800/1800'):
    print("Ah!")
