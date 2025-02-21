import requests
from transformers import pipeline
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK stopwords if not already done
import nltk
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')


# Preprocessing function to clean text
def preprocess_text(text):
    # Lowercase the text
    text = text.lower()
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove stopwords
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return ' '.join(tokens)


# Load a pre-trained BERT model for text classification from Hugging Face Transformers
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
