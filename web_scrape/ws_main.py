from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import csv
import web_scrape.screener as screener
import web_scrape.ticker_tape as ticker_tape
import web_scrape.market_watch as market_watch
import web_scrape.time_news as time_news

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# # Setup Chrome options
# chrome_options = Options()
# chrome_options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# )
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--incognito")

# # Load a custom profile
# chrome_options.add_argument("user-data-dir=selenium_profile")

# # Initialize the WebDriver
# service = Service("chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service, options=chrome_options)


def extract_and_save(stock):

    global current_affairs

    service = Service("chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    name = stock["name"]
    screener_url = stock["screener"]
    ticker_tape_url = stock["tcikertape"]
    market_watch_url = stock["marketwatch"]
    general_info = stock["generalinfo"]

    company_news = ""
    crunching_numbers = ""
    current_affairs = ""

    driver.get(screener_url)
    text = screener.pro_con(driver)
    company_news += text + "\n"

    numbers = screener.top(driver)
    crunching_numbers += numbers + "\n"

    quaterly_table = screener.table_data(driver)
    crunching_numbers += "\n" + quaterly_table

    driver.get(ticker_tape_url)
    text = ticker_tape.table_contents(driver)
    crunching_numbers += text

    text = ticker_tape.extract_forecast_text(driver)
    company_news += "\n" + text

    text = ticker_tape.extract_commentary_text(driver)
    company_news += "\n" + text

    text = ticker_tape.extract_holdings_text(driver)
    company_news += "\n" + text

    text = ticker_tape.extract_dividend_trend_text(driver)
    company_news += "\n" + text

    text = time_news.get_news(driver)
    current_affairs += text

    # text = market_watch.extract_top_headlines(driver, market_watch_url)
    # company_news += "\n" + text

    driver.quit()

    if general_info:
        with open("generalinfo/" + general_info, "r", encoding="utf-8") as gen_file:
            general_info_data = gen_file.read()

    filename = name + ".txt"
    output_filepath = "outputfiles/" + filename

    with open(output_filepath, "w", encoding="utf-8") as file:
        file.write("Initial information about the company\n")
        file.write(general_info_data + "\n")
        file.write("Current Financial Analysis\n")
        file.write(crunching_numbers + "\n")
        file.write("Current Company News\n")
        file.write(company_news + "\n")
        file.write("General Current Affairs\n")
        file.write(current_affairs + "\n")

    data = (
        "Initial information about the company\n"
        + general_info_data
        + "\n"
        + "Current Financial Analysis\n"
        + crunching_numbers
        + "\n"
        + "Current Company News\n"
        + company_news
        + "\n"
        + "General Current Affairs\n"
        + current_affairs
        + "\n"
    )

    return crunching_numbers, data


def read_stock_data_from_csv(csv_file):
    stock_data = []
    with open(csv_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stock_data.append(row)
    return stock_data


def run_now(s):
    csv_file = f"web_scrape/stock_links.csv"
    stock_data = read_stock_data_from_csv(csv_file)
    for stock in stock_data:
        if s == stock["stockcode"]:
            crunching_numbers, filename = extract_and_save(stock)
            break
    return crunching_numbers, filename
