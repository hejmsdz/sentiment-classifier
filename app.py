from flask import Flask, request, abort, jsonify
from classifier import Classifier

classifier = Classifier('model/tokenizer.json', 'model/rnn.h5')
app = Flask(__name__)

@app.route('/prediction')
def prediction():
    text = request.args.get('text')
    if not text:
        return abort(400)
    category, confidence = classifier.classify(text)
    return jsonify(category=category, confidence=confidence)
