from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import screener
import ticker_tape
import market_watch
import time_news

service = Service("chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

screener_url = "https://www.screener.in/company/INFY/consolidated/"

ticker_tape_url = "https://www.tickertape.in/stocks/infosys-INFY"

market_watch_url = "https://www.marketwatch.com/investing/stock/infy?mod=search_symbol"

company_news = ""
crunching_numbers = ""
current_affairs = ""

text = screener.pro_con(driver, screener_url)
company_news += text + "\n"

numbers = screener.top(driver, screener_url)
crunching_numbers += numbers + "\n"

quaterly_table = screener.table_data(driver, screener_url)
crunching_numbers += "\n" + quaterly_table


text = ticker_tape.table_contents(driver, ticker_tape_url)
crunching_numbers += text

text = ticker_tape.extract_forecast_text(driver, ticker_tape_url)
company_news += "/n" + text

text = ticker_tape.extract_commentary_text(driver, ticker_tape_url)
company_news += "/n" + text

text = ticker_tape.extract_holdings_text(driver, ticker_tape_url)
company_news += "/n" + text

text = ticker_tape.extract_dividend_trend_text(driver, ticker_tape_url)
company_news += "/n" + text

# text = market_watch.extract_top_4_headlines(driver, market_watch_url)
# company_news += "/n" + text

text = time_news.get_news(driver)
current_affairs += text

driver.quit()

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(crunching_numbers + "\n")
    file.write(company_news + "\n")
    file.write(current_affairs + "\n")
