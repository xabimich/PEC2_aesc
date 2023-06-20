from flask import jsonify
import pandas as pd
import pickle
import numpy as np
import json
from my_model.predict import make_prediction

#
#        model = pickle.load(f)

args ='{ "data": {"alcohol": 9.4, "density": 0.56, "pH": 3.2 }}'
X = json.loads(args)
X = X['data']
print(X)
columns_model = ['alcohol', 'fixed acidity', 'volatile acidity',
                         'citric acid', 'residual sugar', 'chlorides',
                         'free sulfur dioxide', 'total sulfur dioxide', 
                         'density', 'pH', 'sulphates']
        # Simplificamos las columnas a 3 para el testing 
selected_data = {column: X.get(column, 0) for column in columns_model}
print(selected_data)
selected_df = pd.DataFrame([selected_data])
print(selected_df)
# Make predictions using the selected columns

prediction = make_prediction(input_data=selected_df)

print(prediction['predictions'][0])