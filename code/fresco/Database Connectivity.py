def main():
    conn = sqlite3.connect('SAMPLE.db')
    #create connection cursor
    cursor = conn.cursor()
    
    #create table ITEMS using the cursor
    sql1 = 'DROP TABLE IF EXISTS ITEMS'
    sql2 = '''

       CREATE TABLE ITEMS (
       item_id INT(6) NOT NULL,
       item_name CHAR(20) NOT NULL,
       item_description CHAR(20) NOT NULL,
       item_category CHAR(20) NOT NULL,
       quantity_in_stock INT
       )
      '''

    #commit connection 
    cursor.execute(sql1)
    cursor.execute(sql2)

    #close connection
    conn.close()


'''To test the code, no input is required'''
if __name__ == "__main__":