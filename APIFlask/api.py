from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
import json
from my_model.predict import make_prediction

app = Flask(__name__)

@app.route('/wine', methods=['POST'])
def wine():
    data = request.get_json()
    X = data['data']
    columns_model = ['alcohol', 'fixed acidity', 'volatile acidity',
                     'citric acid', 'residual sugar', 'chlorides',
                     'free sulfur dioxide', 'total sulfur dioxide', 
                     'density', 'pH', 'sulphates']
    # Simplificamos las columnas a 3 para el testing 
    selected_data = {column: X.get(column, 0) for column in columns_model}
    
    selected_df = pd.DataFrame([selected_data])
    
    prediction = make_prediction(input_data=selected_df)
    prediction = prediction['predictions'][0]
    if prediction == 1:
        prediction = "bad"
    else:
        prediction = "good"
    return jsonify(prediction), 200

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=int("5000"))