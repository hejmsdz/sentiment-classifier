import json
import pickle

from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model

from preprocess import preprocess

class Classifier:
    CATEGORIES = ['negative', 'neutral', 'positive']

    def __init__(self, tokenizer_file, model_file):
        self.load_tokenizer(tokenizer_file)
        self.load_model(model_file)
    
    def load_tokenizer(self, path):
        with open(path) as f:
            data = json.load(f)
            self.tokenizer = tokenizer_from_json(data)
    
    def load_model(self, path):
        self.model = load_model(path)
        self.max_words = self.model.input.shape[1]
    
    def classify(self, text):
        text = preprocess(text)
        test_seq = self.tokenizer.texts_to_sequences([text])
        test_seq = sequence.pad_sequences(test_seq, maxlen=self.max_words)
        probabilities = self.model.predict_proba(test_seq)[0, :]
        category_index = probabilities.argmax()
        category_name = self.CATEGORIES[category_index]
        confidence = float(probabilities[category_index])
        return category_name, confidence



