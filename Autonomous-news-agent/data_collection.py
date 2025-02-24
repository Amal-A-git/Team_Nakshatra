import requests
import spacy
from summarization import preprocess_text, classifier
from transformers import pipeline



# Function to fetch news articles based on user query
def fetch_articles(query, api_key):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)

    # Check if the response status is OK (200)
    if response.status_code == 200:
        data = response.json()
        if 'articles' in data:
            return data['articles']
        else:
            print("No 'articles' key found in the response.")
            return []
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

# Function to summarize an article using Hugging Face Transformers
def summarize_article(article_text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  # Pre-trained summarization model
    summary = summarizer(article_text, max_length=1024, min_length=300, do_sample=False)
    return summary[0]['summary_text']

# Function to publish an article to WordPress
def publish_to_wordpress(title, content, wordpress_url, username, password):
    # Endpoint for creating posts
    endpoint = f"{wordpress_url}/wp-json/wp/v2/posts"

    # Post data
    post_data = {
        "title": title,
        "content": content,
        "status": "publish"  # Automatically publish the post
    }

    # Basic authentication with username and application password
    response = requests.post(endpoint, json=post_data, auth=(username, password))

    if response.status_code == 201:  # 201 Created
        print(f"Article '{title}' published successfully!")
        print(f"URL: {response.json().get('link')}")
    else:
        print(f"Failed to publish article '{title}'.")
        print(f"Error: {response.status_code} - {response.text}")
