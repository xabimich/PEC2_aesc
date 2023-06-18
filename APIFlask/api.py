from flask import Flask, jsonify, request
import numpy as np
import json
from my_model.predict import make_prediction

app = Flask(__name__)

@app.route('/wine', methods=['POST'])
def wine_classifier():
    data = request.get_json()
    input_data = np.array(data['data'])
    prediction = make_prediction(input_data=input_data)
    if prediction == 1:
        prediction = "good"
    else:
        prediction = "bad"
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
