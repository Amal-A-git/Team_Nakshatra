import requests
import spacy
from summarization import preprocess_text, classifier


# Replace with your NewsAPI key
api_key = '07a36934c738460fbc6c776a126ec7cf'
url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={api_key}'

# Function to fetch news articles
def fetch_articles(url):
    response = requests.get(url)

    # Check if the response status is OK (200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if 'articles' key exists
        if 'articles' in data:
            return data['articles']
        else:
            print("No 'articles' key found in the response.")
            return []
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


# Function to classify articles based on keywords
def classify_article(article_text):
    # Define keywords for each category
    categories = {
        "Sports": ["match", "tournament", "player", "goal", "cricket", "football"],
        "Politics": ["government", "election", "policy", "minister", "parliament"],
        "Current Events": ["incident", "breaking", "crime", "accident", "protest"],
        "Technology": ["AI", "technology", "software", "hardware", "innovation"]
    }

    # Initialize an empty list for assigned categories
    assigned_categories = []

    # Check for keywords in the article text and assign categories
    for category, keywords in categories.items():
        if any(keyword.lower() in article_text.lower() for keyword in keywords):
            assigned_categories.append(category)

    return assigned_categories if assigned_categories else ["Current News"]

# Fetch articles from NewsAPI
articles = fetch_articles(url)

# Process and classify each article
if articles:
    for article in articles:
        title = article['title']  # Extract the title of the article
        print(f"Title: {title}")
        # Keyword-based classification
        keyword_categories = classify_article(title)
        print(f"Keyword-Based Categories: {keyword_categories}")

# Preprocess the title before classification (optional, depending on model needs)
        processed_title = preprocess_text(title)

        # Classify the title using the Hugging Face BERT classifier
        classification_result = classifier(processed_title)

        # Print classification result (label and score)
        print(f"Classification: {classification_result}")
        print("-" * 50)
else:
    print("No articles found.")
