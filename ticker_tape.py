from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def preprocess_table(l):
    text = ""
    for i in range(0, len(l), 2):
        for j in range(len(l[i])):
            text += l[i][j] + " " + l[i + 1][j] + "\n"
    return text


def table_contents(driver, url):
    driver.get(url)
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


def extract_forecast_text(driver, url):
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-2004670762"))
    )
    forecast_div = driver.find_element(By.CLASS_NAME, "jsx-2004670762.forecast-radial")

    perc_value = forecast_div.find_element(By.CLASS_NAME, "percBuyReco-value").text

    recommendation_text = forecast_div.find_element(
        By.CSS_SELECTOR, ".d-flex-col .typography-body-medium-m"
    ).text
    analysts_info = forecast_div.find_element(By.CSS_SELECTOR, ".d-flex-col p").text

    x = "percentage" + perc_value + recommendation_text + analysts_info
    return x


def extract_commentary_text(driver, url):
    driver.get(url)
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

        description = item.find_element(By.CLASS_NAME, "commentary-desc").text.strip()

        results.append({"header": header, "description": description})
        l = results
        text = ""
        for i in l:
            text += i["header"] + " : " + i["description"] + "\n"

    return text


def extract_holdings_text(driver, url):
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-1970749611"))
    )

    screensplit_contents = driver.find_element(
        By.CLASS_NAME, "jsx-1970749611.screensplit-contents"
    )

    results = ""

    sections = screensplit_contents.find_elements(By.CLASS_NAME, "screensplit-elem")
    for section in sections:
        section_title = section.find_element(
            By.CLASS_NAME, "holding-title"
        ).text.strip()
        commentary_items = section.find_elements(By.CLASS_NAME, "commentary-item-root")

        for item in commentary_items:
            header = item.find_element(By.TAG_NAME, "h4").text.strip()

            description = item.find_element(
                By.CLASS_NAME, "commentary-desc"
            ).text.strip()

            results += section_title + " : " + header + " : " + description + "\n"

    return results


def extract_dividend_trend_text(driver, url):
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jsx-3946593877"))
    )

    dividend_trend_container = driver.find_element(
        By.CLASS_NAME, "jsx-3946593877.commentary-container"
    )

    results = ""

    commentary_items = dividend_trend_container.find_elements(
        By.CLASS_NAME, "commentary-item-root"
    )
    for item in commentary_items:
        header = item.find_element(By.TAG_NAME, "h4").text.strip()
        description = item.find_element(By.CLASS_NAME, "commentary-desc").text.strip()

        results += "dividend Trend : " + header + " : " + description + "\n"

    return results
