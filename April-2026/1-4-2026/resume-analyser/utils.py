import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt')
nltk.download('stopwords')

def preprocess(text):
    #lowercase
    text= text.lower()

    #tokenization
    words= word_tokenize(text)
    #remove stop words and punctuation
    stop_words=set(stopwords.words('english'))

    filtered_words=[
        word for word in words 
        if word not in stop_words and word not in string.punctuation
    ]

    return ' '.join(filtered_words)