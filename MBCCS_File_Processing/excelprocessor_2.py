import os
import time
from xlrd import open_workbook, xldate
from datetime import datetime
from MBCCS_File_Processing import config

from xlrd.sheet import ctype_text
import re
import cx_Oracle

user = config.user
pw = config.pw
dsn = config.dsn
tablename_ship_hist = config.tablename_ship_hist
tablename_ship_hist_natl = config.tablename_ship_hist_natl
sqlst_ship_hist = "INSERT INTO " + \
        tablename_ship_hist + \
        "(FILE_NAME, CRUISE_DATE, SHIP, SHIP_TYPE, CALL_TYPE, SHIP_TOTAL) " \
        "VALUES (" \
        ":1,    " \
        ":2,    " \
        ":3,    " \
        ":4 ,    " \
        ":5,    " \
        ":6)"

sqlst_ship_hist_natl = "INSERT INTO " + \
        tablename_ship_hist_natl + \
        "(SHIP_HIST_FILE_NAME, NATL, QTY) " \
        "VALUES (" \
        ":1,    " \
        ":2,    " \
        ":3)"

con = cx_Oracle.connect(user, pw, dsn)
cursor = con.cursor()

path_nationality_breakdown = config.path_nationality_breakdown
files_nationality = os.listdir(path_nationality_breakdown)
file_nationality = files_nationality[0]
list_ship_hist = []
list_ship_hist_natl = []


nationality = ['SINGAPORE', 'ARGENTINA', 'AUSTRALIA', 'AUSTRIA', 'BANGLADESH', 'BELGIUM', 'BRAZIL', 'BRUNEI', 'BULGARIA', 'CAMBODIA', 'CANADA', 'CHILE', 'CHINA', 'COLOMBIA', 'COSTA RICA', 'CROATIA', 'CZECH REPUBLIC', 'DENMARK', 'DOMINICAN REPUBLIC', 'EGYPT', 'FINLAND', 'FRANCE', 'GERMANY', 'GREECE', 'HONG KONG', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA', 'IRAN', 'IRELAND', 'ISRAEL', 'ITALY', 'JAPAN', 'KAZAKHSTAN', 'KENYA', 'KOREA', 'KUWAIT', 'LAOS', 'LATVIA', 'LITHUANIA', 'LUXEMBOURG', 'MACAU', 'MALAYSIA', 'MAURITIUS', 'MEXICO', 'MYANMAR', 'NEPAL', 'NETHERLANDS', 'NEW ZEALAND', 'NORWAY', 'PAKISTAN', 'PERU', 'PHILIPPINES', 'POLAND', 'PORTUGAL', 'ROMANIA', 'RUSSIA', 'SLOVAKIA', 'SLOVENIA', 'SOUTH AFRICA', 'SPAIN', 'SRI LANKA', 'SWEDEN', 'SWITZERLAND', 'TAIWAN', 'TANZANIA', 'THAILAND', 'TURKEY', 'UAE', 'UKRAINE', 'UK', 'USA', 'VENEZUELA', 'VIETNAM', 'OTHERS']
col_file_name = None
col_cruise_date = datetime.today()
col_ship = None
col_ship_type = None
col_call_type = None
col_ship_total = 0

col_natl = None
col_qty = 0

dtmode = None

for file_nationality in files_nationality:
    count_ship_hist = 0
    count_ship_hist_natl = 0
    print(file_nationality)
    # table column
    col_file_name = file_nationality

    file_nationality_path = os.path.join(path_nationality_breakdown, file_nationality)
    excelbook = open_workbook(file_nationality_path)
    dtmode = excelbook.datemode

    if excelbook.sheet_by_name('Summary'):
        sheet_summary = excelbook.sheet_by_name('Summary')
        # print('# of rows {0}, # of columns {1}'.format(sheet_summary.nrows, sheet_summary.ncols))
        for row_idx in range(8, sheet_summary.nrows):
            current_row = sheet_summary.row_values(row_idx, 2, sheet_summary.ncols)
            if '<date>' in current_row or not current_row[0]:
                break
            # print(current_row[0:10])
            for idx, cell in enumerate(current_row):
                if idx == 0:
                    col_cruise_date = (xldate.xldate_as_datetime(cell, dtmode)).date()
                elif idx == 1:
                    col_ship = cell
                elif idx == 2:
                    col_ship_type = cell
                elif idx == 3:
                    col_call_type = cell
                elif idx == 4:
                    col_ship_total = int(cell)
                    # print('col_cruise_date {0}, col_ship {1}, col_ship_type {2}, col_call_type {3}, col_ship_total {4}'
                    #       .format(col_cruise_date, col_ship, col_ship_type, col_call_type, col_ship_total))
                    list_ship_hist.append((col_file_name,
                                           col_cruise_date,
                                           col_ship,
                                           col_ship_type,
                                           col_call_type,
                                           col_ship_total))
                    count_ship_hist += 1
                elif idx > 4 and cell > 0:
                    list_ship_hist_natl.append((col_file_name, nationality[idx-5], int(cell)))
                    count_ship_hist_natl += 1
        print('# of ship hist {0}, # of natl {1}'.format(count_ship_hist, count_ship_hist_natl))
        # print(list_ship_hist)
        # print(list_ship_hist_natl)

print('size of list_ship_hist {0},\r\nsize of list_ship_hist_natl {1}'.format(len(list_ship_hist), len(list_ship_hist_natl)))
start_time = time.clock()
cursor.prepare(sqlst_ship_hist)
cursor.executemany(None, list_ship_hist)
middle_time = time.clock()
cursor.prepare(sqlst_ship_hist_natl)
cursor.executemany(None, list_ship_hist_natl)
end_time = time.clock()
cursor.close()
con.commit()
con.close()

print('timing1 {0}, timing2 {1}'.format(middle_time - start_time,end_time - middle_time ))





