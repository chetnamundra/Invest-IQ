from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import random


# Define a function for random delays to mimic human interaction
def random_delay(min_delay=1, max_delay=3):
    time.sleep(random.uniform(min_delay, max_delay))


# Define a function to extract top headlines
def extract_top_headlines(driver, url):
    driver.get(url)
    random_delay()  # Add a random delay

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

    # Extract details from the top articles
    for article in article_elements[:10]:
        random_delay()  # Add a random delay

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
