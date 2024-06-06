from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_url(driver, text):
    try:
        driver.get("https://www.screener.in/")

        # Wait for the input element for the search to be clickable
        input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'input[data-company-search="true"]')
            )
        )

        # Clear any existing text in the input field
        input_element.clear()

        # Enter the search text into the input element
        input_element.send_keys(text)

        # Click on the first suggestion in the dropdown (if available)
        try:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "ul.dropdown-content a.button")
                )
            ).click()
        except:
            # If no suggestion is available, submit the form by pressing Enter
            input_element.submit()

        # Wait for the new page to load
        WebDriverWait(driver, 10).until(EC.url_contains("/company/"))

        # Get the current URL of the page after search
        url = driver.current_url
        print("URL after search:", url)
        return url

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        # Close the WebDriver session
        driver.quit()


# Example usage:
# Initialize the WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome()

# Example search text
search_text = "infy"

# Call the function to get the URL after searching for the text
search_url = get_url(driver, search_text)
