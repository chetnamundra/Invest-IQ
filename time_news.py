from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_news(driver):
    driver.get("https://economictimes.indiatimes.com")

    container = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "pageContent"))
    )

    items = WebDriverWait(container, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.newsList li"))
    )

    headlines = []
    headline_text = ""
    for item in items:
        try:
            anchor_tag = item.find_element(By.TAG_NAME, "a")

            headline = anchor_tag.text.strip()
            if headline != "":
                headlines.append(headline)
        except Exception as e:
            print(f"Failed to extract headline: {e}")

    for idx, headline in enumerate(headlines, start=1):
        # print(f"{idx}. {headline}")
        headline_text += f"{idx}. {headline}" + "\n"

    return headline_text
