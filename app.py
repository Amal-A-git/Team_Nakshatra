from flask import Flask, request, jsonify, render_template
import requests
from transformers import pipeline
import os

app = Flask(__name__)

# Initialize the BERT summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
api_key=''
# Function to fetch news articles from NewsAPI
def fetch_articles(query):
    api_key = os.getenv('NEWSAPI_KEY')  # Retrieve API key from environment variables
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        return []


# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    query = data.get('query')

    if not query:
        return jsonify({"error": "Query is required"}), 400

    # Fetch and summarize articles
    articles = fetch_articles(query,api_key)
    summaries = []
    for article in articles[:1]:  # Limit to top 5 articles
        title = article['title']
        content = article['content'] or article['description']
        if content:
            summary = summarizer(content, max_length=1000, min_length=500, do_sample=False)[0]['summary_text']
            summaries.append({"title": title, "summary": summary})
        else:
            summaries.append({"title": title, "summary": "Content not available"})

    return jsonify(summaries)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Default to port 10000 if PORT is not set
    app.run(host='0.0.0.0', port=port)
