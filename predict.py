# -*- coding: utf-8 -*-
"""predict.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15Uit-p65N1SkxCo3RanNfjzxPjXbs000
"""

import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

with open('trained_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # ... preprocess input data (if needed)
    prediction = model.predict([[data['feature1'], data['feature2'], ...]])  # Adjust features
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)