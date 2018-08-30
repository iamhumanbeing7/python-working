import os, re
from xlrd import open_workbook
import cx_Oracle
from MBCCS_File_Processing import config
import shutil


def removeNonAscii(varstring):
    return "".join(i for i in varstring if ord(i) < 128)

user = config.user
pw = config.pw
dsn = config.dsn
path_2016 = config.path_2016
files_2016 = os.listdir(path_2016)
# print(files_2016)

# print("Database version:", con.version)
# i = 1
sqlst = "INSERT INTO " + config.tablename_temp + " VALUES (" \
        ":FILE_NAME,    " \
        ":CRUISE_INFO,    " \
        ":RESOURCE1,    " \
        ":RESOURCE1_CONTENT ,    " \
        ":RESOURCE1_QTY,    " \
        ":RESOURCE2,    " \
        ":RESOURCE2_CONTENT ,    " \
        ":RESOURCE2_QTY,    " \
        ":RESOURCE3,    " \
        ":RESOURCE3_CONTENT,    " \
        ":RESOURCE3_QTY, " \
        ":EXCEPTION_INFO, " \
        ":QTY_APO, " \
        ":QTY_SA," \
        ":YR)"
con = cx_Oracle.connect(user, pw, dsn)
cursor = con.cursor()
cursor.prepare(sqlst)
i = 0
for file_2016 in files_2016:
    i += 1
    file_2016_path = os.path.join(path_2016, file_2016)
    print(file_2016)
    excelbook = open_workbook(file_2016_path)
    var_cruise_info = ''
    var_resource1 = "SA"
    var_resource1_content = ""
    var_resource1_qty = 0

    var_resource2 = "APO"
    var_resource2_content = ""
    var_resource2_qty = 0

    var_resource3 = "TSA"
    var_resource3_content = ""
    var_resource3_qty = 0

    var_cell_content = ""
    SA_IND = False
    APO_IND = False

    var_qty_APO = 0
    var_qty_SA = 0

    for sheet in excelbook.sheets():
        # process Main tab
        if sheet.name.upper() == 'MAIN':
            var_cruise_info = sheet.cell(0, 0).value
        elif sheet.name.upper() == 'BILLING':
            var_qty_APO = int(sheet.cell(sheet.nrows - 1, 3).value)
            var_qty_SA = int(sheet.cell(sheet.nrows - 1, 7).value)
        elif sheet.name.upper().strip() in ['TIMESHEET','APO SA TIMESHEET']:
            sheet_apo_sa_col = sheet.col_values(1, 1)
            # process APO and SA timesheet
            for cell in sheet_apo_sa_col:
                # while sheet_apo_sa.cell(var_rowno, var_colno) and sheet_apo_sa.cell(var_rowno, var_colno).value:
                # print("row no: {0}, column no: {1}".format(var_rowno, var_colno))
                if cell:
                    if cell == "DIRECT TO MBCCS" or cell == "DIRECT TO MBCC":
                        SA_IND = True
                        APO_IND = False
                        continue
                    elif cell == "AFT/SICC TO MBCCS":
                        APO_IND = True
                        SA_IND = False
                        continue
                    elif cell.upper() == "NAME":
                        continue
                else:
                    continue
                # start counting of SA/APO officers
                if SA_IND:
                    # SA officer increased by 1
                    var_resource1_content += cell + "\n"
                    var_resource1_qty += 1
                    # print(var_resource1_qty)
                    # print(cell)
                elif APO_IND:
                    # APO officer increased by 1
                    var_resource2_content += cell + "\n"
                    var_resource2_qty += 1
        elif sheet.name.upper().strip() == 'TSA TIMESHEET':
            # process sheet 3, i.e. TSA timesheet
            sheet_tsa_col = sheet.col_values(4, 3)
            for cell_TSA in sheet_tsa_col:

                if cell_TSA and re.match('\d{4}/\d{4}', cell_TSA):
                    var_resource3_content += cell_TSA + "\n"
                    var_resource3_qty += 1
                    # print(var_resource3_qty)
                    # print(cell_TSA)
                else:
                    continue

    var_resource1_content = removeNonAscii(var_resource1_content)
    var_resource2_content = removeNonAscii(var_resource2_content)
    var_resource3_content = removeNonAscii(var_resource3_content)

    try:
        cursor.execute(None,
                       FILE_NAME=file_2016,
                       CRUISE_INFO=var_cruise_info,
                       RESOURCE1=var_resource1,
                       RESOURCE1_CONTENT=var_resource1_content,
                       RESOURCE1_QTY=var_resource1_qty,
                       RESOURCE2=var_resource2,
                       RESOURCE2_CONTENT=var_resource2_content,
                       RESOURCE2_QTY=var_resource2_qty,
                       RESOURCE3=var_resource3,
                       RESOURCE3_CONTENT=var_resource3_content,
                       RESOURCE3_QTY=var_resource3_qty,
                       EXCEPTION_INFO='',
                       QTY_APO=var_qty_APO,
                       QTY_SA=var_qty_SA,
                       YR='2016')
    # except cx_Oracle.DatabaseError as exception:
    #     print('Failed to execute cursor!')
    #     print("DatabaseError error: {0}".format(exception))
    except Exception as commonexception:
        print('{0} cannot be processed due to Exception : {1}'.format(file_2016, commonexception))
    # i += 1
        try:
            cursor.execute(None,
                           FILE_NAME=file_2016,
                           CRUISE_INFO='',
                           RESOURCE1='',
                           RESOURCE1_CONTENT='',
                           RESOURCE1_QTY=0,
                           RESOURCE2='',
                           RESOURCE2_CONTENT='',
                           RESOURCE2_QTY=0,
                           RESOURCE3='',
                           RESOURCE3_CONTENT='',
                           RESOURCE3_QTY=0,
                           EXCEPTION_INFO=str(commonexception),
                           QTY_APO=0,
                           QTY_SA=0,
                           YR='2016'
                           )
            print('{0} Only file name and exception information are persisted.'.format(file_2016))
            # shutil.copy(file_2016_path, path_2016_error)
        except Exception as e:
            print('Failed to Insert problematic file name to DB due to Exception: {0}'.format(e))

cursor.close()
con.commit()
con.close()
print('Totally {0} files were processed.'.format(str(i)))