from flask import Flask, request, jsonify
import requests
from transformers import pipeline

app = Flask(__name__)

# Initialize the BERT summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to fetch news articles from NewsAPI
def fetch_articles(query, api_key):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        return []

# Endpoint to handle summarization requests
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    query = data.get('query')
    api_key = data.get('api_key')

    if not query or not api_key:
        return jsonify({"error": "Query and API key are required"}), 400

    # Fetch and summarize articles
    articles = fetch_articles(query, api_key)
    summaries = []
    for article in articles[:5]:  # Limit to top 5 articles
        title = article['title']
        content = article['content'] or article['description']
        if content:
            summary = summarizer(content, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
            summaries.append({"title": title, "summary": summary})
        else:
            summaries.append({"title": title, "summary": "Content not available"})

    return jsonify(summaries)

if __name__ == '__main__':
    app.run(debug=True)
