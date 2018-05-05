import pandas as pd
import xlsxwriter
import os
from openpyxl import load_workbook

def importCSV(filePath):
    df = pd.read_csv(filePath)
    return df

def importExcel(filePath, sheetName):
    df = pd.read_excel(open(filePath,'rb'), sheet_name=sheetName)
    return df;

def convertToExcel(frompath, topath, sheetName):
    df = pd.read_csv(frompath)
    writer = pd.ExcelWriter(topath, engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name=sheetName)
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

def createSheet(path, sheetName, dataFrame):
    book = load_workbook(path)
    writer = pd.ExcelWriter(path, engine='openpyxl')
    writer.book = book
    dataFrame.to_excel(writer, sheet_name=sheetName)
    writer.save()
    writer.close()

def updateFile(df, path):
    df.to_csv(path)

def getAllFiles(path):
    return os.listdir(path)

def createExcel(path, sheetName, df):
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name=sheetName)
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()