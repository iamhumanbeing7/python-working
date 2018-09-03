import os
from xlrd import open_workbook
from MBCCS_File_Processing import config
from xlrd.sheet import ctype_text
import re
import cx_Oracle

user = config.user
pw = config.pw
dsn = config.dsn
tablename_ship_hist = config.tablename_ship_hist
sqlst = "INSERT INTO " + \
        tablename_ship_hist + \
        "(FILE_NAME, CRUISE_DATE, SHIP, SHIP_TYPE, CALL_TYPE, SHIP_TOTAL) " \
        "VALUES (" \
        ":1,    " \
        ":2,    " \
        ":3,    " \
        ":4 ,    " \
        ":5,    " \
        ":6)"

path_nationality_breakdown = config.path_nationality_breakdown
files_nationality = os.listdir(path_nationality_breakdown)
file_nationality = files_nationality[0]
i = 0
nationality = ['SINGAPORE', 'ARGENTINA', 'AUSTRALIA', 'AUSTRIA', 'BANGLADESH', 'BELGIUM', 'BRAZIL', 'BRUNEI', 'BULGARIA', 'CAMBODIA', 'CANADA', 'CHILE', 'CHINA', 'COLOMBIA', 'COSTA RICA', 'CROATIA', 'CZECH REPUBLIC', 'DENMARK', 'DOMINICAN REPUBLIC', 'EGYPT', 'FINLAND', 'FRANCE', 'GERMANY', 'GREECE', 'HONG KONG', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA', 'IRAN', 'IRELAND', 'ISRAEL', 'ITALY', 'JAPAN', 'KAZAKHSTAN', 'KENYA', 'KOREA', 'KUWAIT', 'LAOS', 'LATVIA', 'LITHUANIA', 'LUXEMBOURG', 'MACAU', 'MALAYSIA', 'MAURITIUS', 'MEXICO', 'MYANMAR', 'NEPAL', 'NETHERLANDS', 'NEW ZEALAND', 'NORWAY', 'PAKISTAN', 'PERU', 'PHILIPPINES', 'POLAND', 'PORTUGAL', 'ROMANIA', 'RUSSIA', 'SLOVAKIA', 'SLOVENIA', 'SOUTH AFRICA', 'SPAIN', 'SRI LANKA', 'SWEDEN', 'SWITZERLAND', 'TAIWAN', 'TANZANIA', 'THAILAND', 'TURKEY', 'UAE', 'UKRAINE', 'UK', 'USA', 'VENEZUELA', 'VIETNAM', 'OTHERS']

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
            if (row != nationality):
                print('row != row_pattern: {0}'.format(row))
            if (row_indx != 7):
                print('row_indx != 7: {0}'.format(row_indx))






