# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:07:31 2018

@author: Alex.W
"""

#! python3
# ch14_pp_xlsx2csv.py - convert excel files to csv files

# import modules to be used
import os, openpyxl, csv
os.makedirs('convert_xlsx_csv', exist_ok = True)

# loop through files
for excelFile in os.listdir('.'):
    # skip non_xlsx files, load the workbook object
    if not excelFile.endswith('.xlsx'):
        continue
    print('Converting ' + excelFile + '...')

    wb = openpyxl.load_workbook(excelFile)
    
    for sheetName in wb.sheetnames:
        # loop through every sheet in the workbook
        sheet = wb[sheetName]
        
        # to identify if the sheet is blank sheet
        if sheet.cell(row = sheet.max_row, column = sheet.max_column).value is None:
            continue

        # create csv file name from excelfile and sheetname
        csvFileName = excelFile + sheetName + '.csv'
        csvFileObj = open(os.path.join('convert_xlsx_csv', csvFileName), 'w', newline = '')
        # create csv writer object for this csv file
        csvWriter =csv.writer(csvFileObj)

        for rowNum in range(1, sheet.max_row + 1):
            rowData = []
            # loop through each cell in the row
            for colNum in range(1, sheet.max_column + 1):
                rowData.append(sheet.cell(row = rowNum, column = colNum).value)
            csvWriter.writerow(rowData)
        csvFileObj.close()

print('success')
