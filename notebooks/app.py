from flask import render_template, request, jsonify,Flask
import flask
from flask_restful import Resource, Api, reqparse
import numpy as np
import traceback
import pickle
import pandas as pd
import joblib
from sklearn.preprocessing import PowerTransformer

# App definition
app = Flask(__name__)
api = Api(app)

def totalIncome(df):
    df[['Total_Income']] = df['ApplicantIncome'] + df['CoapplicantIncome']
    return df

log = PowerTransformer()

def log_transform(df):
    log.fit(df[['Total_Income']])
    df['Total_Income'] = log.transform(df[['Total_Income']])
    return df


# importing model
with open('best_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

#webpage

@app.route('/')
def welcome():
   return 'Hello! This api can be used to get loan application status predictions. Please POST your parameters using \/predict'

@app.route('/predict', methods=['POST','GET'])
def predict():

   if flask.request.method == 'GET':
       return 'In order to get a prediction, please use a POST with the following parameters in the body: \
       Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area.'

   if flask.request.method == 'POST':
       try:
        json_data = request.get_json()
        js_df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        # getting predictions from our model.
            
        res = model.predict_proba(js_df)
        # we cannot send numpy array as a result
        return res.tolist()

       except:
           return jsonify({
               'trace': traceback.format_exc()
               })



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555)
