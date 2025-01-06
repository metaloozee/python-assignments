import os
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open('house.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_price():
    try:
        area = float(request.form['area'])
        
        features = np.array([[area]])
        prediction = model.predict(features)[0][0]
        
        if prediction >= 1:
            formatted_prediction = f" {prediction:.2f} Cr"
        else:
            formatted_prediction = f" {prediction * 100:.2f} L"
        
        return render_template('index.html', prediction=formatted_prediction)
    
    except Exception as e:
        return render_template('index.html', prediction="Error in prediction")

if __name__ == '__main__':
    app.run(debug=True)