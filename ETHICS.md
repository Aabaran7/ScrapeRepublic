## Ethical Considerations in Web Scraping

Web scraping involves extracting data from websites, which raises several ethical considerations. This document outlines the primary ethical concerns associated with the Nepali Politics Sentiment Analyzer project and how we've addressed them.

### 1. Respecting Website Terms of Service and Robots.txt

*Consideration:*  
Websites have their own terms of service (ToS) and robots.txt files that dictate how their content can be accessed. Ignoring these rules could lead to legal issues or getting blocked.

*Action Taken:*  
Before diving into the scraping process, we carefully reviewed MyRepublica's ToS and examined their robots.txt file. We noted that the User-agent: * directive is present with an empty Disallow: line, which means all user agents are allowed to access the site. This clarity gave us the green light to proceed with scraping, knowing we were following the website's guidelines.

### 2. Rate Limiting and Server Load

*Consideration:*  
Frequent requests to a website can strain its servers, which may degrade performance for other users.

*Action Taken:*  
Although we confirmed that scraping is allowed, we still planned to incorporate rate limiting in our script, with delays (e.g., time.sleep(2)) between requests to avoid overwhelming MyRepublica’s servers. This step reflects our commitment to ethical scraping practices, ensuring we respect the website's resources.

### 3. Data Privacy and Confidentiality

*Consideration:*  
When scraping, it's essential to think about the privacy of individuals mentioned in the articles. Sensitive personal information should be handled with care.

*Action Taken:*  
We focused solely on publicly available news articles. By adhering to this principle, we avoid collecting sensitive information and ensure we’re respecting the privacy of individuals mentioned in the content.

### 4. Accurate Representation of Sentiment

*Consideration:*  
Sentiment analysis can sometimes misinterpret the tone or intent of the original content, leading to misleading conclusions.

*Action Taken:*  
While we initially planned to use TextBlob for sentiment analysis, we recognize its limitations. With our commitment to ethical practices and the proper representation of content, we’ll be cautious in interpreting sentiment from other sources, ensuring users understand the potential for misinterpretation.

### 5. Purpose and Impact of Data Use

*Consideration:*  
The purpose behind scraping and analyzing data should always align with ethical guidelines. Misuse could lead to misinformation or harm.

*Action Taken:*  
Our goal is to provide insights for educational purposes. Since we're moving forward with scraping MyRepublica, we remain focused on sourcing data responsibly, seeking out alternatives that align with our ethical standards and contribute positively to discussions around political sentiment in Nepal.

### Conclusion

The Nepali Politics Sentiment Analyzer project was designed with the intent to analyze sentiment from MyRepublica articles. After carefully reviewing their robots.txt and ToS, we confirmed that scraping is allowed. This decision reflects our dedication to ethical standards in data usage and respect for website policies. We’re committed to contributing meaningfully to conversations about political sentiment in Nepal through responsible data practices.