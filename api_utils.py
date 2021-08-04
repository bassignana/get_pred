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
            
def insertIntoFOOD(pid ,start ,end,carbs,proteins, fats,comment):
    try:
        sqliteConnection = sqlite3.connect('main.db')
        cur = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO MEAL
                          (ID ,START ,END,CARBS, PROTEINS, FATS, COMMENT) 
                          VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (pid ,start ,end,carbs,proteins, fats,comment)
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
                          (ID ,TIMESTAMP ,VALUE,COMMENT) 
                          VALUES (?, ?, ?, ?, ?);"""

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
            
if __name__=='__main__':
  print("main")
  
  
