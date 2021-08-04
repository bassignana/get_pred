import pickle
from flask import Flask, request
import numpy as np
import pandas as pd
import train

#pickle and unpickle must happen with the same version of scikit learn

ml_api = Flask(__name__)
ml_api.config["DEBUG"] = True

@ml_api.route('/')
def hello_world():
    return 'Hello, World!'

@ml_api.route('/train', methods=["GET"])
def get_pickle():
    train.training()
    return 'training'

@ml_api.route('/predict_svc', methods=["GET"])
def predict_svc():
    
    with open('model_svc.pkl', 'rb') as model_svc_pkl:
        model_svc = pickle.load(model_svc_pkl)
    
    sepal_length = request.args.get("sepal_length")
    sepal_width = request.args.get("sepal_width")
    petal_length = request.args.get("petal_length")
    petal_width = request.args.get("petal_width")

    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model_svc.predict(input_data)
    return str(prediction)


@ml_api.route('/predict_rfc', methods=["GET"])
def predict_rfc():
    
    with open('model_rfc.pkl', 'rb') as model_rfc_pkl:
        model_rfc = pickle.load(model_rfc_pkl)
    
    sepal_length = request.args.get("sepal_length")
    sepal_width = request.args.get("sepal_width")
    petal_length = request.args.get("petal_length")
    petal_width = request.args.get("petal_width")

    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model_rfc.predict(input_data)
    return str(prediction)
