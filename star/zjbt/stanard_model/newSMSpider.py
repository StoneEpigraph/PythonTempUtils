#!/usr/bin/env python3
# coding: utf-8
from openpyxl import Workbook, load_workbook

if __name__ == '__main__':
    wb = load_workbook('./vehicle.xlsx')
    ws = wb.active
    for row in ws:
        print(dir(row))
        for cell in row:
            print(dir(cell))
            print('col_idx: ' + str(cell.col_idx))
            # print('column: ' + str(cell.column))
            if cell.col_idx != 2:
                continue
            print(cell.value)
            raise Exception("手动抛出异常")

# wb.save("sample.xlsx")
