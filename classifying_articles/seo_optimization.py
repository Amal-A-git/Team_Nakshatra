def optimize_for_seo(content, primary_keyword, secondary_keywords):
    # Add primary keyword to the title and first paragraph
    title = f"{primary_keyword}: Latest Updates and News"
    first_paragraph = f"{primary_keyword} has been making headlines recently. {content[:150]}..."
    
    # Include secondary keywords naturally in the body
    body = content
    for keyword in secondary_keywords:
        if keyword not in body:
            body += f" {keyword}."
    
    return {"title": title, "first_paragraph": first_paragraph, "body": body}

# Example usage
content = "Lucknow has seen a rise in crime rates recently. Police are investigating."
primary_keyword = "Lucknow Crime News"
secondary_keywords = ["Uttar Pradesh", "local news", "crime updates"]
optimized_content = optimize_for_seo(content, primary_keyword, secondary_keywords)
print(optimized_content)
