import pickle
from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import train
import api_utils as ut
import sqlite3
import pred
import logging

logging.basicConfig(level=logging.INFO,
                    filename='app.log', filemode='a', 
                    format='%(levelname)s - %(asctime)s - %(filename)s - %(funcName)s - %(message)s')


#pickle and unpickle must happen with the same version of scikit learn
ml_api = Flask(__name__)
ml_api.config["DEBUG"] = True
logging.info("main app started")


# una route vera, che non sia una richiesta api, ci va se no il deploy va in errore
@ml_api.route('/')
def hello_world():
    return 'Hello, World!!'

@ml_api.route('/train', methods=["GET"])
def get_pickle():
    train.training()
    return 'training'

@ml_api.route('/predict_svc', methods=["POST"])
def predict_svc():
    
    with open('model_svc.pkl', 'rb') as model_svc_pkl:#attenzione a non lasciare fuori dalle funzioni nulla se no i comandi vengono eseguiti
        model_svc = pickle.load(model_svc_pkl)
    
    
    json_data = request.get_json()# assicurarsi sempre che la modialià e il formato dei dati in invio sia conforme alla modalità e formato di ricezione

    sepal_length = json_data["sepal_length"]
    sepal_width = json_data["sepal_width"]
    petal_length = json_data["petal_length"]
    petal_width = json_data["petal_width"]

    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model_svc.predict(input_data)
    return str(prediction)




@ml_api.route('/predict_rfc', methods=["POST"])
def predict_rfc():
    
    with open('model_rfc.pkl', 'rb') as model_rfc_pkl:
        model_rfc = pickle.load(model_rfc_pkl)
    
    
    json_data = request.get_json()

    sepal_length = json_data["sepal_length"]
    sepal_width = json_data["sepal_width"]
    petal_length = json_data["petal_length"]
    petal_width = json_data["petal_width"]
    
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model_rfc.predict(input_data)
    return str(prediction)


@ml_api.route('/tables/insert/sleep', methods=['POST'])
def ins_tb_sleep():
    json_data = request.get_json()

    pid = json_data["pid"]
    start = json_data["start"]
    end = json_data["end"]
    quality = json_data["quality"]
    comment = json_data["comment"]
    
    ut.insertIntoSLEEP(pid ,start ,end,quality,comment)
    return jsonify('finished_sleep')

@ml_api.route('/tables/insert/meal', methods=['POST'])
def ins_tb_meal():
    json_data = request.get_json()

    pid = json_data["pid"]
    start = json_data["start"]
    carbs = json_data["carbs"]
    proteins = json_data["proteins"]
    fats = json_data["fats"]
    comment = json_data["comment"]
    
    ut.insertIntoFOOD(pid ,start ,carbs,proteins, fats,comment)
    return jsonify('finished_meal')

@ml_api.route('/tables/insert/glucose', methods=['POST'])
def ins_tb_glucose():
    json_data = request.get_json()

    pid = json_data["pid"]
    timestamp = json_data["timestamp"]
    value = json_data["value"]
    comment = json_data["comment"]
    print((pid ,timestamp, value, comment))
    ut.insertIntoGLUCOSE(pid ,timestamp, value, comment)
    return jsonify('finished glucose')


@ml_api.route('/tables/createall', methods=["GET"])
def tables_create():
    #la creazione del db avviene automaticamente se non esiste 
    conn = sqlite3.connect('main.db')
    #datetime format https://stackoverflow.com/questions/17227110/how-do-datetime-values-work-in-sqlite
    #"YYYY-MM-DD HH:MM:SS.SSS"
    conn.execute('''CREATE TABLE SLEEP
         (ID INTEGER     NOT NULL,
         START           TEXT    NOT NULL,
         FINISH            TEXT     NOT NULL,
         QUALITY        INT,
         COMMENT         VARCHAR(150),
         PRIMARY KEY ( ID, START, FINISH));''')
    conn.execute('''CREATE TABLE MEAL
         (ID INTEGER      NOT NULL,
         START           TEXT    NOT NULL,
         CARBS        INT     NOT NULL,
         PROTEINS        INT,
         FATS        INT,
         COMMENT         VARCHAR(150),
         PRIMARY KEY (ID, START));''')
    conn.execute('''CREATE TABLE GLUCOSE
         (ID INTEGER     NOT NULL,
         PERIOD           TEXT    NOT NULL,
         VALUE            INT NOT NULL     ,
         COMMENT         VARCHAR(150),
         PRIMARY KEY (ID, PERIOD));
         ''')
    conn.close()
    return "Table created successfully"

@ml_api.route("/predict", methods=['GET'])
def predict_script():
    df = pred.create_df_pd(1)
    return df.to_string()

@ml_api.route("/select/glucose", methods=['GET'])
def predict_script2():
    df = ut.sel_glucose()
    return df.to_string()
    


if __name__ == '__main__':
    ml_api.run(host='127.0.0.1', port=5000)
