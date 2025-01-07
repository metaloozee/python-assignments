import os
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from typing import Tuple, Optional

app = Flask(__name__)

MIN_AREA = 600  
MAX_AREA = 50000 

def load_model():
    try:
        with open("house.pkl", "rb") as f:
            return pickle.load(f)
    except Exception as e:
        app.logger.error(f"Failed to load model: {str(e)}")
        return None

def validate_area(area: float) -> Tuple[bool, Optional[str]]:
    if not isinstance(area, (int, float)):
        return False, "Area must be a number"
    if area < MIN_AREA:
        return False, f"Area must be at least {MIN_AREA} sq.ft"
    if area > MAX_AREA:
        return False, f"Area must be less than {MAX_AREA} sq.ft"
    return True, None

def format_price(price: float) -> str:
    if price >= 1:
        return f"{price:.2f} Cr"
    return f"{price * 100:.2f} L"

model = load_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_price():
    try:
        area = float(request.form['area'])
        is_valid, error_message = validate_area(area)
        if not is_valid:
            return render_template('index.html', prediction=error_message)
        
        features = np.array([[area]])
        prediction = model.predict(features)[0]
        if isinstance(prediction, np.ndarray):
            prediction = prediction[0]
        
        formatted_prediction = format_price(prediction)
        return render_template('index.html', prediction=formatted_prediction)
    
    except ValueError:
        return render_template('index.html', prediction="Please enter a valid number")
    except Exception as e:
        app.logger.error(f"Prediction error: {str(e)}")
        return render_template('index.html', prediction="Error in prediction")

if __name__ == '__main__':
    app.run(debug=True)