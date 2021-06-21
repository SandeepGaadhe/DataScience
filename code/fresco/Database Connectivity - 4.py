#!/bin/python3

import sys
import os
import sqlite3


# Complete the function below.

def main():
    conn = sqlite3.connect('SAMPLE.db')
    cursor = conn.cursor()
    cursor.execute("drop table if exists ITEMS")
    
    sql_statement = '''CREATE TABLE ITEMS
    (item_id integer not null, item_name varchar(300), 
    item_description text, item_category text, 
    quantity_in_stock integer)'''
    
    cursor.execute(sql_statement)
    
    items = [(101, 'Nik D300', 'Nik D300', 'DSLR Camera', 3),
             (102, 'Can 1300', 'Can 1300', 'DSLR Camera', 5),
             (103, 'gPhone 13S', 'gPhone 13S', 'Mobile', 10),
             (104, 'Mic canvas', 'Mic canvas', 'Tab', 5),
             (105, 'SnDisk 10T', 'SnDisk 10T', 'Hard Drive', 1)
             ]
    try:
        cursor.executemany("Insert into ITEMS values (?,?,?,?,?)", items)

        #Add code for updating quantity_in_stock
        sql =   '''
                UPDATE ITEMS SET quantity_in_stock = 4 WHERE item_id = 103
                '''
        cursor.execute(sql)

        sql =   '''
                UPDATE ITEMS SET quantity_in_stock = 2 WHERE item_id = 101
                '''
        cursor.execute(sql)

        sql =   '''
                UPDATE ITEMS SET quantity_in_stock = 0 WHERE item_id = 105
                '''
        cursor.execute(sql)

        cursor.execute("select item_id,quantity_in_stock from ITEMS")
    except:
        'Unable to perform the transaction.'
    rowout=[]    
    for row in cursor.fetchall():
        rowout.append(row)
    return rowout    
    conn.close()


'''For testing the code, no input is required'''

if __name__ == "__main__":