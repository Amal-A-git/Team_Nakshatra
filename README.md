# AI Hackathon Project: Nakshatra News

Welcome to the **AI Hackathon Project** repository! This project focuses on building a **News Summarizer** that fetches news articles, summarizes them using transformer models, and integrates seamlessly with deployment platforms like Render or local environments.

---

##  Project Overview

This project aims to:
1. Fetch news articles from APIs or via web scraping.
2. Summarize the news articles using transformer models such as `facebook/bart-large-cnn` or lightweight alternatives.
3. Provide deployment options for running the application locally or on cloud platforms like Render.

---

##  Tech Stack

- **Programming Language**: Python
- **Libraries/Frameworks**:
  - `transformers` for text summarization
  - `requests` for API calls
  - `Flask` or `FastAPI` for backend integration
- **Deployment Options**:
  - [Render](https://render.com/) for cloud hosting
  - Local environment setup

---

## Features

- Fetch news articles using APIs (e.g., NewsAPI) or web scraping.
- Summarize fetched articles using transformer models.
- Lightweight summarization alternatives available (e.g., `distilbart`, `t5-small`).
- Easy-to-deploy solution with support for both local and cloud environments.
