from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def preprocess_table(l):
    text = ""
    for i in range(0, len(l), 2):
        for j in range(len(l[i])):
            text += l[i][j] + " " + l[i + 1][j] + "\n"
    return text


def table_contents(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jsx-3519906982"))
        )
        tables = driver.find_elements(By.CSS_SELECTOR, ".jsx-3519906982 table")

        results = []

        for table in tables:
            headers = table.find_elements(By.CSS_SELECTOR, "thead th")
            header_data = []
            for header in headers:
                header_data.append(header.text.strip())

            results.append(header_data)
            rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")

            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")

                row_data = []

                for cell in cells:
                    row_data.append(cell.text.strip())

                results.append(row_data)
        results = preprocess_table(results)

        return results

    except TimeoutException:
        return "Table contents could not be found due to a timeout."

    except NoSuchElementException:
        return "Table contents could not be found. Element not present on the page."


def extract_forecast_text(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jsx-2004670762"))
        )
        forecast_div = driver.find_element(
            By.CLASS_NAME, "jsx-2004670762.forecast-radial"
        )

        perc_value = forecast_div.find_element(By.CLASS_NAME, "percBuyReco-value").text

        recommendation_text = forecast_div.find_element(
            By.CSS_SELECTOR, ".d-flex-col .typography-body-medium-m"
        ).text
        analysts_info = forecast_div.find_element(By.CSS_SELECTOR, ".d-flex-col p").text

        return f"percentage {perc_value} {recommendation_text} {analysts_info}"

    except TimeoutException:
        return "Forecast text could not be found due to a timeout."

    except NoSuchElementException:
        return "Forecast text could not be found. Element not present on the page."


def extract_commentary_text(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jsx-2510798477"))
        )
        commentary_div = driver.find_element(
            By.CLASS_NAME, "jsx-2510798477.commentary-items"
        )
        commentary_items = commentary_div.find_elements(
            By.CLASS_NAME, "commentary-item-root"
        )

        results = []

        for item in commentary_items:
            header = item.find_element(By.TAG_NAME, "h4").text.strip()
            description = item.find_element(
                By.CLASS_NAME, "commentary-desc"
            ).text.strip()

            results.append(f"{header} : {description}")

        return "\n".join(results)

    except TimeoutException:
        return "Commentary text could not be found due to a timeout."

    except NoSuchElementException:
        return "Commentary text could not be found. Element not present on the page."


def extract_holdings_text(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jsx-1970749611"))
        )

        screensplit_contents = driver.find_element(
            By.CLASS_NAME, "jsx-1970749611.screensplit-contents"
        )

        results = []

        sections = screensplit_contents.find_elements(By.CLASS_NAME, "screensplit-elem")
        for section in sections:
            section_title = section.find_element(
                By.CLASS_NAME, "holding-title"
            ).text.strip()
            commentary_items = section.find_elements(
                By.CLASS_NAME, "commentary-item-root"
            )

            for item in commentary_items:
                header = item.find_element(By.TAG_NAME, "h4").text.strip()
                description = item.find_element(
                    By.CLASS_NAME, "commentary-desc"
                ).text.strip()

                results.append(f"{section_title} : {header} : {description}")

        return "\n".join(results)

    except TimeoutException:
        return "Holdings text could not be found due to a timeout."

    except NoSuchElementException:
        return "Holdings text could not be found. Element not present on the page."


def extract_dividend_trend_text(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jsx-3946593877"))
        )

        dividend_trend_container = driver.find_element(
            By.CLASS_NAME, "jsx-3946593877.commentary-container"
        )

        results = []

        commentary_items = dividend_trend_container.find_elements(
            By.CLASS_NAME, "commentary-item-root"
        )
        for item in commentary_items:
            header = item.find_element(By.TAG_NAME, "h4").text.strip()
            description = item.find_element(
                By.CLASS_NAME, "commentary-desc"
            ).text.strip()

            results.append(f"dividend Trend : {header} : {description}")

        return "\n".join(results)

    except TimeoutException:
        return "Dividend trend text could not be found due to a timeout."

    except NoSuchElementException:
        return (
            "Dividend trend text could not be found. Element not present on the page."
        )


def get_news(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "your-news-class"))
        )
        # Replace 'your-news-class' with the actual class name for the news section
        news_section = driver.find_element(By.CLASS_NAME, "your-news-class")

        news_items = news_section.find_elements(By.CLASS_NAME, "news-item")

        results = []

        for item in news_items:
            news_title = item.find_element(By.CLASS_NAME, "news-title").text.strip()
            news_content = item.find_element(By.CLASS_NAME, "news-content").text.strip()

            results.append(f"{news_title} : {news_content}")

        return "\n".join(results)

    except TimeoutException:
        return "Current affairs text could not be found due to a timeout."

    except NoSuchElementException:
        return (
            "Current affairs text could not be found. Element not present on the page."
        )
