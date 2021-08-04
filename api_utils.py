import sqlite3
import pandas as pd

def insertIntoSLEEP(pid ,start ,end,quality,comment):
    try:
        sqliteConnection = sqlite3.connect('main.db')
        cur = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO SLEEP
                          (ID ,START ,END,QUALITY,COMMENT) 
                          VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (pid ,start ,end,quality,comment)
        cur.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("insert successful")

        cur.close()

    except sqlite3.Error as error:
        print("Failed to insert into sleep table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            
def insertIntoFOOD(pid ,start ,carbs,proteins, fats,comment):
    try:
        sqliteConnection = sqlite3.connect('main.db')
        cur = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO MEAL
                          (ID ,START ,CARBS, PROTEINS, FATS, COMMENT) 
                          VALUES (?, ?, ?, ?,?,?);"""

        data_tuple = (pid ,start ,carbs,proteins, fats,comment)
        cur.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("insert successful")

        cur.close()

    except sqlite3.Error as error:
        print("Failed to insert into meal table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")   
            
def insertIntoGLUCOSE(pid ,timestamp, value, comment):
    try:
        sqliteConnection = sqlite3.connect('main.db')
        cur = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO MEAL
                          (ID ,PERIOD ,VALUE,COMMENT) 
                          VALUES (?, ?, ?, ?);"""

        data_tuple = (pid ,timestamp, value, comment)
        cur.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("insert successful")

        cur.close()

    except sqlite3.Error as error:
        print("Failed to insert into glucose table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def create_df_pd(pid):
    """
    pid = id number
    """
    query = """SELECT
        sleep.start as sleep_start,
        sleep.end as sleep_end,
        sleep.quality as quality,
        meal.start as meal_start,
        meal.end as meal_end,
        meal.carbs as carbs,
        meal.proteins as proteins,
        meal.fats as fats,
        glucose.period as period,
        glucose.value as value
    FROM
        SLEEP
        INNER JOIN MEAL ON SLEEP.id = MEAL.id
        INNER JOIN GLUCOSE ON MEAL.id = GLUCOSE.id"""

    condition = " WHERE SLEEP.ID = " + str(pid)

    df = pd.read_sql_query(query+condition, con)
    return df


if __name__=='__main__':
  print("main")
  
  
