import xlrd
from library.config import Config


def read_locators(sheetname):
    workbook = xlrd.open_workbook(Config.LOC_PATH)
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    header = next(rows)
    d = {}
    for row in rows:
        d[row[0].value] = (row[1].value, row[2].value)

    return d
print(read_locators('reg_objects'))


