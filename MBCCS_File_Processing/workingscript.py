import os
from xlrd import open_workbook
from MBCCS_File_Processing import config
from xlrd.sheet import ctype_text
import re
#
# path_2018 = config.path_2018
# tempvar = ['a', 'b', 'c', 'd']
# print(tempvar[3])
path_nationality_breakdown = config.path_nationality_breakdown
files_nationality = os.listdir(path_nationality_breakdown)
file_nationality = files_nationality[0]
i = 0
row_patten = ['empty colume', 'S/N', 'Date', 'Ship', 'Ship Type', 'Call Type', 'Ship Total', 'SINGAPORE', 'ARGENTINA', 'AUSTRALIA', 'AUSTRIA', 'BANGLADESH', 'BELGIUM', 'BRAZIL', 'BRUNEI', 'BULGARIA', 'CAMBODIA', 'CANADA', 'CHILE', 'CHINA', 'COLOMBIA', 'COSTA RICA', 'CROATIA', 'CZECH REPUBLIC', 'DENMARK', 'DOMINICAN REPUBLIC', 'EGYPT', 'FINLAND', 'FRANCE', 'GERMANY', 'GREECE', 'HONG KONG', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA', 'IRAN', 'IRELAND', 'ISRAEL', 'ITALY', 'JAPAN', 'KAZAKHSTAN', 'KENYA', 'KOREA', 'KUWAIT', 'LAOS', 'LATVIA', 'LITHUANIA', 'LUXEMBOURG', 'MACAU', 'MALAYSIA', 'MAURITIUS', 'MEXICO', 'MYANMAR', 'NEPAL', 'NETHERLANDS', 'NEW ZEALAND', 'NORWAY', 'PAKISTAN', 'PERU', 'PHILIPPINES', 'POLAND', 'PORTUGAL', 'ROMANIA', 'RUSSIA', 'SLOVAKIA', 'SLOVENIA', 'SOUTH AFRICA', 'SPAIN', 'SRI LANKA', 'SWEDEN', 'SWITZERLAND', 'TAIWAN', 'TANZANIA', 'THAILAND', 'TURKEY', 'UAE', 'UKRAINE', 'UK', 'USA', 'VENEZUELA', 'VIETNAM', 'OTHERS']

for file_nationality in files_nationality[0]:
    print(file_nationality)
    file_nationality_path = os.path.join(path_nationality_breakdown, file_nationality)
    excelbook = open_workbook(file_nationality_path)
    if excelbook.sheet_by_name('Summary'):
        sheet_summary = excelbook.sheet_by_name('Summary')
        rows = sheet_summary.row_values(8, 2, 82)
        for row_indx in range(sheet_summary.nrows):
            row = sheet_summary.row_values(row_indx)
            if 'Ship Total' not in row:
                continue
            if (row != row_patten):
                print('row != row_pattern: {0}'.format(row))
            if (row_indx != 7):
                print('row_indx != 7: {0}'.format(row_indx))






