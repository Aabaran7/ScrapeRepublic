import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib3
import re
import requests
import time
from textblob import TextBlob

# Disable InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def construct_article_link(title):
    # Convert title to lowercase, replace spaces with dashes, and remove special characters
    slug = re.sub(r'[^a-zA-Z0-9\s]', '', title).lower().replace(' ', '-')
    return f"https://myrepublica.nagariknetwork.com/news/{slug}/"

def scrape_politics_articles(base_url, pages=3):
    articles = []

    for page in range(1, pages + 1):
        url = f"{base_url}?page={page}"
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.content, 'html.parser')

        for article in soup.find_all('div', class_='main-heading'):
            title_elem = article.find('h2')
            title = title_elem.text.strip() if title_elem else 'No title'
            full_link = construct_article_link(title)

            # Fetch the full article content
            article_response = requests.get(full_link, verify=False)
            article_soup = BeautifulSoup(article_response.content, 'html.parser')
            content_elem = article_soup.find_all('p')
            content = ' '.join([p.text.strip() for p in content_elem]) if content_elem else 'No content'

            date_elem = article.find('p', class_='headline-time')
            date = date_elem.text.strip() if date_elem else 'No date'

            articles.append({
                'Title': title,
                'Link': full_link,
                'Date': date,
                'Content': content
            })

            time.sleep(2)

    return articles

# Base URL of myRepublica politics section
base_url = 'https://myrepublica.nagariknetwork.com/category/politics'

# Scrape political articles from the first 10 pages
politics_data = scrape_politics_articles(base_url)

# Create a DataFrame
df = pd.DataFrame(politics_data)

# Display the first few rows of the DataFrame
print(df.head())

# Save the DataFrame to a CSV file
df.to_csv('myrepublica_politics_articles.csv', index=False)
print(f"Scraped {len(df)} articles and saved to 'myrepublica_politics_articles.csv'")

def analyze_sentiment(text):
  """Analyzes the sentiment of a given text using TextBlob."""
  analysis = TextBlob(text)
  if analysis.sentiment.polarity > 0:
    return 'Positive'
  elif analysis.sentiment.polarity < 0:
    return 'Negative'
  else:
    return 'Neutral'

def analyze_articles_for_person(df, person_name):
  """Searches for articles mentioning a specific person and analyzes their sentiment."""

  relevant_articles = []
  for index, row in df.iterrows():
    if person_name.lower() in row['Title'].lower():
      relevant_articles.append(row)

  sentiment_results = []
  for article in relevant_articles:
    sentiment = analyze_sentiment(article['Content'])
    sentiment_results.append({
        'Title': article['Title'],
        'Link': article['Link'],
        'Date': article['Date'],
        'Sentiment': sentiment
    })

  return sentiment_results

person_name = input("Enter the last name of the person you want to analyze: ")
sentiment_results = analyze_articles_for_person(df, person_name)

if sentiment_results:
  print(f"\nSentiment analysis for articles mentioning {person_name}:")
  for result in sentiment_results:
    print(f"Title: {result['Title']}")
    print(f"Link: {result['Link']}")
    print(f"Date: {result['Date']}")
    print(f"Sentiment: {result['Sentiment']}\n")
else:
  print(f"No articles found mentioning {person_name}.")