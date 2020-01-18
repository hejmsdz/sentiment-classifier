from flask import Flask, render_template, request, abort, jsonify
from classifier import Classifier

classifier = Classifier('model/tokenizer.json', 'model/rnn.h5')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    text = request.args.get('text')
    if not text:
        return abort(400)
    category, confidence = classifier.classify(text)
    return jsonify(category=category, confidence=confidence)
