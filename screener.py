from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def pro_con(driver):

    analysis_element = driver.find_element(By.ID, "analysis")
    analysis_text = analysis_element.text

    return analysis_text


def preprocess_text(l):
    text = ""
    c = 0

    s = l.split("\n")
    for i in s:
        if c == 0:
            text += i
            c = 1
        else:
            text += " " + i + "\n"
            c = 0
    return text


def preprocess_table(l):
    text = ""
    for i in l:
        for j in i:
            for k in j:
                text += k
            text += "\n"
        text += "\n"
    return text


def top(driver):

    top_element = driver.find_element(By.ID, "top")
    ul_elements = top_element.find_elements(By.TAG_NAME, "ul")
    ul_texts = [ul.text for ul in ul_elements]
    ul_texts = preprocess_text(ul_texts[0])

    return ul_texts


def table_data(driver):

    section_element = driver.find_element(By.ID, "profit-loss")
    tables = section_element.find_elements(By.CLASS_NAME, "ranges-table")

    table_data = []
    for table in tables:
        table_content = []
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            headers = row.find_elements(By.TAG_NAME, "th")
            cells = row.find_elements(By.TAG_NAME, "td")
            cell_texts = [header.text for header in headers] + [
                cell.text for cell in cells
            ]
            table_content.append(cell_texts)
        table_data.append(table_content)

    table_data = preprocess_table(table_data)
    return table_data
