import streamlit as st
from g4f.client import Client
from web_scrape.ws_main import run_now
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Initialize the chatbot client
client = Client()


# Function to fetch stock data
def chart(stock):
    start_date = datetime(2020, 1, 1)
    end_date = datetime.today().date()

    stock_data = yf.download(stock, start=start_date, end=end_date)

    fig, ax = plt.subplots()
    stock_data["Close"].plot(ax=ax, label="Close Price")

    # Customize plot
    plt.title(f"Historical Close Prices of {stock}", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Close Price", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()

    return fig


# Function to get AI response
def ai_response(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": text
                + " Give Reply in 1 or 2 lines only and answer in english",
            }
        ],
    )
    return response.choices[0].message.content


# Function to get AI update
def ai_update(ai_data, selected_stock):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": ai_data
                + f" Given all this info, do analysis and tell me if I should invest in {selected_stock} for the long term currently or not? ",
            }
        ],
    )
    return response.choices[0].message.content


# Streamlit app
def main():
    st.title("Stock Recommendation")

    stock_options = [
        "HDFCBANK.NS",
        "IRCTC",
        "INFY",
        "ICICIBANK",
        "TCS",
        "RELIANCE",
        "HINDUNILVR",
        "ASIANPAINT",
        "BAJFINANCE",
        "MARUTI",
    ]

    selected_stock = st.selectbox("Select a stock", [""] + stock_options)

    if selected_stock:
        st.write("You selected:", selected_stock)

        # Fetch stock data only once when stock is selected
        financial_data, ai_data = run_now(selected_stock)

        # Display AI analysis after web scraping
        st.header("AI Analysis after WebScraping")
        st.write(ai_update(ai_data, selected_stock))

        st.write()
        st.header("Some more Financial Analysis")
        st.write(financial_data)

        st.header("Recent Stock History")
        st.pyplot(chart(selected_stock))

    st.header("AI Chatbot for Stocks")
    user_input = st.text_input("You:", "")
    if st.button("Ask"):
        if user_input:
            st.text_area("ChatBot:", value=ai_response(user_input), height=200)
        else:
            st.warning("Please enter something.")


if __name__ == "__main__":
    main()
