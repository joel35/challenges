import os
import urllib.request
import string
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_harry_most_common_word():
    symbols = string.punctuation
    stop_words = [word.strip() for word in open(stopwords_file, encoding='utf-8')]
    text = open(harry_text, 'r', encoding='utf-8').read().strip().lower().replace('\n', ' ')
    text = ''.join((char for char in text if char not in symbols))
    text = [word for word in text.split() if word not in stop_words]
    return Counter(text).most_common(1)[0]
