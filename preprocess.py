import re
from nltk.tokenize.casual import casual_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
import string

stops = {'in', 'of', 'at', 'a', 'the', 'to', 'on', 'and', 'it'}
stops.update(string.punctuation)
stops.difference_update('?!')

lemmatizer = WordNetLemmatizer()

def tag_for_lemmatizer(tag):
    if tag.startswith('NN'):
        return 'n'
    if tag.startswith('VB'):
        return 'v'
    return 'a'

def preprocess(text):
    if not text or type(text) != str:
        return ''

    text = text.lower()
    text = re.sub(r"https?://[^\s]+", '', text) # hyperlinks
    text = re.sub(r"\@\w+", '', text) # mentions
    text = re.sub(r"#", '', text) # hashtags
    text = re.sub(r"\d+\w*", '', text) # numbers
    text = re.sub(r"'s", '', text) # possesive
    text = re.sub(r"n't", ' not', text) # contractions
    text = re.sub(r"'m", ' am', text)
    text = re.sub(r"'s", ' is', text)
    text = re.sub(r"'re", ' are', text)
    
    words = [word for word in casual_tokenize(text) if word not in stops]
    words = [
        lemmatizer.lemmatize(word, tag_for_lemmatizer(tag))
        for word, tag in pos_tag(words)
    ]
    text = ' '.join(words)
    return text
