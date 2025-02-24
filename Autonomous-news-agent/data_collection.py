import requests
import spacy
from summarization import preprocess_text, classifier
from transformers import pipeline

# # Replace with your NewsAPI key
# api_key = '07a36934c738460fbc6c776a126ec7cf'
# url = f'https://newsapi.org/v2/top-headlines?={query}&apiKey={api_key}'

# # # Function to fetch news articles
# def fetch_articles(url):
#     response = requests.get(url)

#     # Check if the response status is OK (200)
#     if response.status_code == 200:
#         # Parse the JSON response
#         data = response.json()

#         # Check if 'articles' key exists
#         if 'articles' in data:
#             return data['articles']
#         else:
#             print("No 'articles' key found in the response.")
#             return []
#     else:
#         print(f"Error: {response.status_code} - {response.text}")
#         return []


# # Function to classify articles based on keywords
# def classify_article(article_text):
#     # Define keywords for each category
#     categories = {
#         "Sports": ["match", "tournament", "player", "goal", "cricket", "football"],
#         "Politics": ["government", "election", "policy", "minister", "parliament"],
#         "Current Events": ["incident", "breaking", "crime", "accident", "protest"],
#         "Technology": ["AI", "technology", "software", "hardware", "innovation"]
#     }

#     # Initialize an empty list for assigned categories
#     assigned_categories = []

#     # Check for keywords in the article text and assign categories
#     for category, keywords in categories.items():
#         if any(keyword.lower() in article_text.lower() for keyword in keywords):
#             assigned_categories.append(category)

#     return assigned_categories if assigned_categories else ["Current News"]

# # Fetch articles from NewsAPI
# articles = fetch_articles(url)

# # Process and classify each article
# if articles:
#     for article in articles:
#         title = article['title']  # Extract the title of the article
#         print(f"Title: {title}")
#         # Keyword-based classification
#         keyword_categories = classify_article(title)
#         print(f"Keyword-Based Categories: {keyword_categories}")

# # Preprocess the title before classification (optional, depending on model needs)
#         processed_title = preprocess_text(title)

#         # Classify the title using the Hugging Face BERT classifier
#         classification_result = classifier(processed_title)

#         # Print classification result (label and score)
#         print(f"Classification: {classification_result}")
#         print("-" * 50)
# else:
#     print("No articles found.")

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

# Main function to handle user input and output summarized articles
def main():
    # Replace with your NewsAPI key
    api_key = '07a36934c738460fbc6c776a126ec7cf'
    # Get user query
    query = input("Enter your query (e.g., Uttar Pradesh): ")

    # Fetch articles based on the query
    articles = fetch_articles(query, api_key)

    if articles:
        print(f"\nSummarized Articles for Query: {query}\n")
        for i, article in enumerate(articles[:1]):  # Summarize top 5 articles
            title = article['title']
            content = article['content'] or article['description']  # Use content or description for summarization

            if content:
                summary = summarize_article(content)
                print(f"Article {i+1}: {title}")
                print(f"Summary: {summary}")
                print("-" * 50)
            else:
                print(f"Article {i+1}: {title}")
                print("Summary: Content not available.")
                print("-" *150)
    else:
        print("No articles found for your query.")

# Run the program
if __name__ == "__main__":
    main()