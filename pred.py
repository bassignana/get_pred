import pandas as pd
import sqlite3

def create_df_pd(pid):
    """
    pid = id number
    """
    con = sqlite3.connect("main.db")
    query = """SELECT
        sleep.start as sleep_start,
        sleep.finish as sleep_end,
        sleep.quality as quality,
        meal.start as meal_start,
        meal.carbs as carbs,
        meal.proteins as proteins,
        meal.fats as fats,
        glucose.period as period,
        glucose.value as value
    FROM
        SLEEP
        INNER JOIN MEAL ON SLEEP.id = MEAL.id
        INNER JOIN GLUCOSE ON MEAL.id = GLUCOSE.id"""
    condition = " WHERE SLEEP.ID = " + str(pid) + " ;"
        
    df = pd.read_sql_query(query+condition, con)
    con.commit()
    con.close()
    return df



if __name__=='__main__':
    create_df_pd()
    create_df_pd2()

    
