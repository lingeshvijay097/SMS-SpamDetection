import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stem = PorterStemmer()


def preprocess1(data):
    msg = []
    for i in range(0, len(data)):
        msg1 = re.sub('[^a-zA-Z]', ' ', data[i])
        msg1 = msg1.lower()
        msg1 = msg1.split()
        msg1 = [stem.stem(word) for word in msg1 if not word in stopwords.words('english')]
        msg1 = ' '.join(msg1)
        msg.append(msg1)
    return msg
