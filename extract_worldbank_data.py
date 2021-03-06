#!/usr/bin/env python

import xlrd
import MySQLdb as mdb
import yaml
from pprint import pprint


# Initialise mysql connection from own config file
# Example config file is given in config_example.yaml
with open('config.yaml', 'r') as f:
    config = yaml.load(f)


# Define connection
con = mdb.connect(config['hostname'], 
                  config['username'], 
                  config['password'], 
                  config['database']
                  )

    
def who_data_to_db(data):
    
    with con:

        cur = con.cursor()
        sql = "INSERT INTO world_bank_tb_data (country_code, year, tb_count) VALUES (%s, %s, %s)"
        cur.execute(sql, (data['country_code'], data['year'], data['tb_count']))


def extract_who_data():

    # Define Excel file, open workbook and get main worksheet
    filename = 'Data/WorldBank/API_SH.TBS.INCD_DS2_en_excel_v2.xls' 
    book = xlrd.open_workbook(filename)
    main_sheet = book.sheet_by_index(0)

    # Start looping through data at 5th row
    for row_id in range(4, main_sheet.nrows):  

        print ('-'*40)
        print ('Row: %s' % row_id)

        country_name = main_sheet.cell(row_id, 0).value
        country_code = main_sheet.cell(row_id, 1).value

        for x in xrange(34,59):

            year = 1956 + x

            if main_sheet.cell(row_id, x).value:
                count = int(main_sheet.cell(row_id, x).value)
            else:
                count = None

            data = {'country_code': country_code, 
                    'year': year,
                    'tb_count': count}

            pprint(data)
            who_data_to_db(data)


def who_metadata_to_db(data):

    with con:

        cur = con.cursor()

        sql = "INSERT INTO world_bank_metadata_countries (country_code, region, income_group, notes, tablename) VALUES (%s, %s, %s, %s, %s)"

        cur.execute(sql, (data['country_code'], data['region'], data['income_group'], data['notes'], data['tablename']))


def extract_who_metadata():

   # Define Excel file, open workbook and get main worksheet
    filename = 'Data/WorldBank/API_SH.TBS.INCD_DS2_en_excel_v2.xls' 
    book = xlrd.open_workbook(filename)
    main_sheet = book.sheet_by_index(1)

    for row_id in range(1, main_sheet.nrows):  

        print ('-'*40)
        print ('Row: %s' % row_id)

        for col_id in range(0, main_sheet.ncols):  # Iterate through columns
            cell_obj = main_sheet.cell(row_id, col_id)  # Get cell object by row, col
            print ('Column: [%s] cell_obj: [%s]' % (col_id, cell_obj))

        if main_sheet.cell(row_id, 0).value:
            country_code = main_sheet.cell(row_id, 0).value
        else:
            country_code = None

        if main_sheet.cell(row_id, 1).value:
            region = main_sheet.cell(row_id, 1).value
        else:
            region = None

        if main_sheet.cell(row_id, 2).value:            
            income_group = main_sheet.cell(row_id, 2).value
        else:
            income_group = None

        if main_sheet.cell(row_id, 3).value:
            notes = main_sheet.cell(row_id, 3).value
        else:
            notes = None

        if main_sheet.cell(row_id, 4).value:
            tablename = main_sheet.cell(row_id, 4).value
        else:
            tablename = None

        data = {'country_code': country_code, 
                'region': region, 
                'income_group': income_group, 
                'notes': notes,
                'tablename': tablename}
        
        pprint(data)
        data_to_db(data)


def main():
    
    extract_who_metadata()
    extract_who_data()


if __name__ == '__main__':
    main()
