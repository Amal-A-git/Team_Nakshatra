import requests

def publish_to_wordpress(title, content, api_url, username, password):
    headers = {
        'Content-Type': 'application/json'
    }
    
    data = {
        'title': title,
        'content': content,
        'status': 'publish'
    }
    
    response = requests.post(api_url + "/wp-json/wp/v2/posts",
                             json=data,
                             auth=(username, password),
                             headers=headers)
    
    if response.status_code == 201:
        print("Article published successfully!")
        print("URL:", response.json()['link'])
    else:
        print("Failed to publish article:", response.status_code)

# Example usage
api_url = "https://yourwordpresssite.com"
username = "your_username"
password = "your_password"
publish_to_wordpress(
    title=optimized_content['title'],
    content=optimized_content['first_paragraph'] + optimized_content['body'],
    api_url=api_url,
    username=username,
    password=password
)
