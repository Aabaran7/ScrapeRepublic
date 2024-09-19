# ScrapeRepublica

This project is designed to analyze the sentiment expressed in Nepali news articles about specific political figures. It focuses on scraping articles from the "Politics" section of the MyRepublica news website ([https://myrepublica.nagariknetwork.com](https://myrepublica.nagariknetwork.com)). The MyRepublica news website is a Nepali news outlet.

## Features

- **Web Scraping:** The script employs `requests` to fetch web pages and `BeautifulSoup` to parse the HTML content. It extracts the following information from each article:
    - Title
    - Link
    - Date
    - Content
- **Sentiment Analysis:** The project utilizes `TextBlob`, a natural language processing library, to determine the sentiment polarity of each article's content. The sentiment is classified as:
    - Positive
    - Negative
    - Neutral
- **Data Storage:**  The scraped articles are organized into a Pandas DataFrame and saved as a CSV file (`myrepublica_politics_articles.csv`) for easy access and further analysis.
- **Person-Specific Analysis:** The script allows users to input the last name of a political figure. It then filters the articles to include only those mentioning the specified individual and performs sentiment analysis on those articles.

## Libraries Used

- `requests`: For fetching web pages.
- `beautifulsoup4`: For parsing HTML content.
- `pandas`: For data manipulation and storage.
- `urllib3`: For managing HTTP connections.
- `textblob`: For natural language processing and sentiment analysis.

## How to Run

1.  **Install Libraries:** Make sure you have the necessary libraries installed. You can install them using pip: "bash pip install beautifulsoup4 requests pandas urllib3 textblob"
2.  **Run the Code:** Execute the Python script in a Jupyter Notebook (Google Colab is recommended) or a similar environment.
3.  **Enter Name:** The script will prompt you to enter the last name of the politician you want to analyze.
4.  **View Results:** The script will display the sentiment analysis results for the articles mentioning the specified politician. Each result will include:
    - Title of the article
    - Link to the article
    - Date of publication
    - Sentiment (Positive, Negative, or Neutral)

## Disclaimer

- This project is intended for educational and research purposes only.
- Please respect the terms of service of MyRepublica and any other websites you scrape.
- Sentiment analysis is not always accurate and should be considered an approximation. The results should be interpreted with caution.

## Potential Improvements

- **Enhanced Scraping:** Implement more robust scraping techniques to handle potential changes in website structure.
- **Scraping a Larger Data Set:** Add additional historical articles beyond the first 10 pages of the website.
- **Advanced Sentiment Analysis:** Explore more sophisticated sentiment analysis models and techniques for improved accuracy.
- **Named Entity Recognition:** Integrate NER to identify and analyze sentiment towards specific entities mentioned in the articles.
- **Data Visualization:** Create visualizations to represent the sentiment analysis results in a more engaging and informative way.

## Contributors

- Ian Chen
- Aabaran Paudel
- Gemini LOL

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

