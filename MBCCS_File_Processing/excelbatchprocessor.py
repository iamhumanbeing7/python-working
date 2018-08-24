import os
from xlrd import open_workbook
import cx_Oracle


def addsinglequote(stringvar):
    return "'" + stringvar + "'"


# import db_config
user = "APPTESTDBA"
pw = "Passw0rd1"
dsn = "SSCDA/oradbdev"
path_2017 = "D:\\Work\AA_Projects\\2018-06_MBCCS\\Requirements\\Data\\MBCCS Security Deployment_fromBenny\\2017\\"
files_2017 = os.listdir(path_2017)
# print(files_2017)

# print("Database version:", con.version)
i = 1
sqlst = "INSERT INTO TBL_MBCCS_SECURITY_TEAM_RAW VALUES (" \
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
        ":EXCEPTION_INFO)"

con = cx_Oracle.connect(user, pw, dsn)
cursor = con.cursor()
cursor.prepare(sqlst)

for file_2017 in files_2017:
    # if i == 3:
    #     break
    print(file_2017)
    excelbook = open_workbook(os.path.join(path_2017, file_2017))

    try:
        sheet_main = excelbook.sheet_by_index(0)
        sheet_apo_sa = excelbook.sheet_by_index(2)
        sheet_apo_sa_col = sheet_apo_sa.col_values(1, 1)
        sheet_tsa = excelbook.sheet_by_index(3)
        sheet_tsa_col = sheet_tsa.col_values(4, 3)

        var_cruise_info = sheet_main.cell(0, 0).value
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

        # process sheet 2, i.e. APO and SA
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
            elif APO_IND:
                # APO officer increased by 1
                var_resource2_content += cell + "\n"
                var_resource2_qty += 1

        # process sheet 3, i.e. TSA sheet
        for cell_TSA in sheet_tsa_col:
            if cell_TSA:
                var_resource3_content += cell_TSA + "\n"
                var_resource3_qty += 1
            else:
                continue

        cursor.execute(None,
                       FILE_NAME=file_2017,
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
                       EXCEPTION_INFO='')
    # except cx_Oracle.DatabaseError as exception:
    #     print('Failed to execute cursor!')
    #     print("DatabaseError error: {0}".format(exception))
    except Exception as commonexception:
        print('{0} cannot be processed due to Exception : {1}'.format(file_2017, commonexception))
    # i += 1
        try:
            cursor.execute(None,
                           FILE_NAME=file_2017,
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
                           EXCEPTION_INFO=str(commonexception))
            print('{0} Only file name and exception information are persisted.'.format(file_2017))
        except Exception as e:
            print('Failed to Insert problematic file name to DB due to Exception: {0}'.format(e))

cursor.close()
con.commit()
con.close()
