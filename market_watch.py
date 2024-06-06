from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def extract_top_4_headlines(driver, url):
    driver.get(url)

    # Wait until the main news container is loaded
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "j-moreHeadlineWrapper"))
    )

    # Locate the main news container
    news_container = driver.find_element(By.CLASS_NAME, "j-moreHeadlineWrapper")

    # Locate all article elements within the news container
    article_elements = news_container.find_elements(By.CLASS_NAME, "element--article")

    results = []
    text = ""

    # Extract details from the top 4 articles
    for article in article_elements[:4]:
        # Extract the headline
        headline = article.find_element(By.CLASS_NAME, "article__headline").text.strip()

        # Extract the link
        link = (
            article.find_element(By.CLASS_NAME, "article__headline")
            .find_element(By.TAG_NAME, "a")
            .get_attribute("href")
        )

        # Extract the timestamp
        timestamp = article.find_element(
            By.CLASS_NAME, "article__timestamp"
        ).get_attribute("data-est")

        # Extract the author
        author = article.find_element(By.CLASS_NAME, "article__author").text.strip()

        results.append(
            {
                "headline": headline,
                "link": link,
                "timestamp": timestamp,
                "author": author,
            }
        )
        text += timestamp + " : " + headline + "\n"

    return text
