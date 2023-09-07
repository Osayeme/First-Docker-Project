"""
from flask import Flask, jsonify, request
from utilities import predict_pipeline

app = Flask(__name__)

@app.route('/predict', methods = ["POST"])
def predict():
    data = request.json
    try:
        sample = data['text']
    except KeyError:
        return jsonify({'error': 'No text sent'})

    sample = [sample]
    predictions = predict_pipeline(sample)
    try:
        result = jsonify(predictions[0])
    except TypeError as e:
        result = jsonify({'error': str(e)})
    return result

if __name__ == '__main__':
    app.run(debug= False)"""

from flask import Flask, render_template, request, jsonify
from utilities import predict_pipeline

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=["POST"])
def predict():
    try:
        sample = request.form['text']
    except KeyError:
        return jsonify({'error': 'No text sent'})

    sample = [sample]
    predictions = predict_pipeline(sample)
    try:
        result = predictions[0]
    except TypeError as e:
        result = str(e)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=False)
