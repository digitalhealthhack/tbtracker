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

    
def data_to_db(data):
    
    with con:

        cur = con.cursor()

        sql = "INSERT INTO who_data_dictionary (variable_name, dataset, code_list, definition) VALUES (%s, %s, %s, %s)"

        cur.execute(sql, (data['name'], data['dataset'], data['code_list'], data['definition']))


def read_who_excel():

    # Define Excel file, open workbook and get main worksheet
    filename = 'Data/WHO/TB_data_dictionary_2016-05-07.xls' 
    book = xlrd.open_workbook(filename)
    main_sheet = book.sheet_by_index(0)

    # Loop through all rows, starting from second row (first is headers)
    for row_id in range(1, main_sheet.nrows):  

        print ('-'*40)
        print ('Row: %s' % row_id)

        for col_id in range(0, main_sheet.ncols):  # Iterate through columns
            cell_obj = main_sheet.cell(row_id, col_id)  # Get cell object by row, col
            print ('Column: [%s] cell_obj: [%s]' % (col_id, cell_obj))

        # Get specific datapoints to add to database
        data = dict()
        data['name'] = main_sheet.cell(row_id, 0).value
        data['dataset'] = main_sheet.cell(row_id, 1).value
        data['code_list'] = main_sheet.cell(row_id, 2).value
        data['definition'] = main_sheet.cell(row_id, 3).value

        pprint(data)
        data_to_db(data)


def main():
    
    data = read_who_excel()


if __name__ == '__main__':
    main()
