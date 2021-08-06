import sqlite3
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO,
                    filename='app.log', filemode='a', 
                    format='%(levelname)s - %(asctime)s - %(filename)s - %(funcName)s - %(message)s')


def insertIntoSLEEP(pid ,start ,end,quality,comment):
    try:
        sqliteConnection = sqlite3.connect('main.db')
        cur = sqliteConnection.cursor()
        logging.info("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO SLEEP
                          (ID ,START ,FINISH,QUALITY,COMMENT) 
                          VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (pid ,start ,end,quality,comment)
        cur.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        logging.info("insert successful")

        cur.close()

    except sqlite3.Error as error:
        logging.exception(error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            logging.info("The SQLite connection is closed")
            
def insertIntoFOOD(pid ,start ,carbs,proteins, fats,comment):
    try:
        sqliteConnection = sqlite3.connect('main.db')
        cur = sqliteConnection.cursor()
        logging.info("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO MEAL
                          (ID ,START ,CARBS, PROTEINS, FATS, COMMENT) 
                          VALUES (?, ?, ?, ?,?,?);"""

        data_tuple = (pid ,start ,carbs,proteins, fats,comment)
        cur.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        logging.info("insert successful")

        cur.close()

    except sqlite3.Error as error:
        logging.exception(error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            logging.info("The SQLite connection is closed")   
            
def insertIntoGLUCOSE(pid ,timestamp, value, comment):
    try:
        
        sqliteConnection = sqlite3.connect('main.db')
        cur = sqliteConnection.cursor()
        logging.info("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO GLUCOSE
                          (ID ,PERIOD ,VALUE,COMMENT) 
                          VALUES (?, ?, ?, ?);"""

        data_tuple = (pid ,timestamp, value, comment)
        
        cur.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        logging.info("Insert successful")

        cur.close()

    except sqlite3.Error as error:
        #questa versione mi fa vedere l'errore su reqbin
        #logging.exception("failed insert glucose")("Failed to insert into glucose table", error)
        #reqbin 200 ma errore nei log
        logging.exception(error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            logging.info("The SQLite connection is closed")
         
    

def sel_table(table):
    con = sqlite3.connect("main.db")
    query = "SELECT * FROM " + str(table)
    df = pd.read_sql_query(query, con)
    con.commit()
    con.close()
    return df


if __name__=='__main__':
  print("main")
  
  
