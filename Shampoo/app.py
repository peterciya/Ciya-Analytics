from flask import Flask, jsonify
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

sarima_model = joblib.load('sarima_model.pkl')

df = pd.read_csv('shampoo_sales.csv')
train, test = df[:24], df[24:]

steps = len(test)
test['Month'] = test['Month'].astype('datetime64[s]')

@app.route('/')
def home():
    return "Welcome to the SARIMA API"

@app.route('/predict', methods=['GET']) 
def predict(): 
    forecast = sarima_model.get_forecast(steps=steps) 
    predictions = np.exp(forecast.predicted_mean)
    prediction_series = pd.Series(predictions, index= test['Month'])
    print(prediction_series)
    
    return jsonify({ 'Predictions': prediction_series.to_dict()})  

if __name__ == '__main__': app.run(debug=True)