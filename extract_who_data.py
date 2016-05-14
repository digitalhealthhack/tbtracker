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

        sql = "INSERT INTO who_tb_burden_countries_20160507 (country, iso2, iso3, iso_numeric, who_region, year, e_pop_num, e_prev_100k, e_prev_100k_lo, e_prev_100k_hi, e_prev_num, e_prev_num_lo, e_prev_num_hi, e_inc_100k, e_inc_100k_lo, e_inc_100k_hi, e_inc_num, e_inc_num_lo, e_inc_num_hi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        cur.execute(sql, (  data['country'], 
                            data['country_iso2'], 
                            data['country_iso3'], 
                            data['iso_numeric'], 
                            data['who_region'], 
                            data['year'], 
                            data['e_pop_num'], 
                            data['e_prev_100k'], 
                            data['e_prev_100k_lo'], 
                            data['e_prev_100k_hi'], 
                            data['e_prev_num'], 
                            data['e_prev_num_lo'], 
                            data['e_prev_num_hi'], 
                            data['e_inc_100k'], 
                            data['e_inc_100k_lo'], 
                            data['e_inc_100k_hi'], 
                            data['e_inc_num'], 
                            data['e_inc_num_lo'], 
                            data['e_inc_num_hi'], 
                            ))


def read_who_excel():

    # Define Excel file, open workbook and get main worksheet
    filename = 'Data/WHO/TB_burden_countries_2016-05-07.xls' 
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
        # Initially only need limited set of data from the sheet
        if main_sheet.cell(row_id, 0).value:
            country = main_sheet.cell(row_id, 0).value
        else: 
            country = None

        if main_sheet.cell(row_id, 1).value:
            country_iso2 = main_sheet.cell(row_id, 1).value
        else:
            country_iso2 = None

        if main_sheet.cell(row_id, 2).value:
            country_iso3 = main_sheet.cell(row_id, 2).value
        else:
            country_iso3 = None

        if main_sheet.cell(row_id, 3).value:
            iso_numeric = main_sheet.cell(row_id, 3).value
        else: 
            iso_numeric = None

        if main_sheet.cell(row_id, 4).value:
            who_region = main_sheet.cell(row_id, 4).value
        else:
            who_region = None

        if main_sheet.cell(row_id, 5).value:
            year = main_sheet.cell(row_id, 5).value
        else:
            year = None

        if main_sheet.cell(row_id, 6).value:
            e_pop_num = main_sheet.cell(row_id, 6).value
        else: 
            e_pop_num = None

        if main_sheet.cell(row_id, 7).value:
            e_prev_100k = main_sheet.cell(row_id, 7).value
        else:
            e_prev_100k = None

        if main_sheet.cell(row_id, 8).value:
            e_prev_100k_lo = main_sheet.cell(row_id, 8).value
        else:
            e_prev_100k_lo = None

        if main_sheet.cell(row_id, 9).value:
            e_prev_100k_hi = main_sheet.cell(row_id, 9).value
        else:
            e_prev_100k_hi = None

        if main_sheet.cell(row_id, 10).value:
            e_prev_num = main_sheet.cell(row_id, 10).value
        else:
            e_prev_num = None

        if main_sheet.cell(row_id, 11).value:
            e_prev_num_lo = main_sheet.cell(row_id, 11).value
        else:
            e_prev_num_lo = None

        if main_sheet.cell(row_id, 12).value:
            e_prev_num_hi = main_sheet.cell(row_id, 12).value
        else:
            e_prev_num_hi = None

        if main_sheet.cell(row_id, 27).value:
            e_inc_100k = main_sheet.cell(row_id, 27).value
        else:
            e_inc_100k = None

        if main_sheet.cell(row_id, 28).value:
            e_inc_100k_lo = main_sheet.cell(row_id, 28).value
        else:
            e_inc_100k_lo = None

        if main_sheet.cell(row_id, 29).value:
            e_inc_100k_hi = main_sheet.cell(row_id, 29).value
        else:
            e_inc_100k_hi = None

        if main_sheet.cell(row_id, 30).value:
            e_inc_num = main_sheet.cell(row_id, 30).value
        else:
            e_inc_num = None

        if main_sheet.cell(row_id, 31).value:
            e_inc_num_lo = main_sheet.cell(row_id, 31).value
        else:
            e_inc_num_lo = None

        if main_sheet.cell(row_id, 32).value:
            e_inc_num_hi = main_sheet.cell(row_id, 32).value
        else:
            e_inc_num_hi = None

        # Define data dictionary
        data = {'country': country, 
                'country_iso2': country_iso2, 
                'country_iso3': country_iso3, 
                'iso_numeric': iso_numeric, 
                'who_region': who_region,
                'year': year,
                'e_pop_num': e_pop_num,
                'e_prev_100k': e_prev_100k, 
                'e_prev_100k_lo': e_prev_100k_lo,
                'e_prev_100k_hi': e_prev_100k_hi,
                'e_prev_num': e_prev_num, 
                'e_prev_num_lo': e_prev_num_lo,
                'e_prev_num_hi': e_prev_num_hi,
                'e_inc_100k': e_inc_100k, 
                'e_inc_100k_lo': e_inc_100k_lo,
                'e_inc_100k_hi': e_inc_100k_hi,
                'e_inc_num': e_inc_num, 
                'e_inc_num_lo': e_inc_num_lo,
                'e_inc_num_hi': e_inc_num_hi,
                }

        # Add data from single row to database
        pprint(data)
        data_to_db(data)


def main():
    
    data = read_who_excel()


if __name__ == '__main__':
    main()
