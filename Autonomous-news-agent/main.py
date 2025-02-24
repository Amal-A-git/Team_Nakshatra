
from data_collection import fetch_articles, summarize_article, publish_to_wordpress
def main():
    # Replace with your NewsAPI key
    api_key = '07a36934c738460fbc6c776a126ec7cf'
    # Replace with your WordPress credentials and site URL
    wordpress_url = "https://nakshatranews.wordpress.com"
    username = "your_username"
    password = "your_application_password"
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
                       # Publish summarized article to WordPress
                publish_to_wordpress(title=title, content=summary, wordpress_url=wordpress_url, username=username, password=password)
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