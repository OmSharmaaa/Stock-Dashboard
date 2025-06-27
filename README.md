# Stock-Dashboard
Developed an interactive stock market dashboard using Streamlit, integrating yFinance for historical pricing, Alpha Vantage for financial statements, and stocknews for sentiment analysis. Added dynamic charts, performance metrics, and robust error handling.

🚀 [Live Demo](https://stock-dashboard-ov7ftwqqcfhcyfwbsrzpjo.streamlit.app/)

# 📊 Stock Analysis Dashboard

An interactive financial dashboard built using Streamlit that allows users to analyze historical stock prices, fundamental data, and real-time news sentiment.

## 🚀 Features

- 📈 **Price Visualization**
  - Interactive line chart using Plotly
  - Adjustable ticker and date range
- 📊 **Pricing Metrics**
  - Daily return, annual return, standard deviation, and risk-adjusted return
- 🧾 **Fundamental Data**
  - Balance Sheet, Income Statement, Cash Flow (via Alpha Vantage API)
  - Smart error handling for rate limits
- 📰 **News Sentiment**
  - Top 10 recent news headlines with sentiment scores
- ✅ Default ticker FORD (`F`) and 1-year range preloaded
- 📤 Exportable pricing data with Streamlit UI

## 📦 Tech Stack
- Python, Streamlit, Plotly
- yFinance for price data
- Alpha Vantage for financial statements
- stocknews for headline scraping and sentiment

## 🛠 How to Run
```bash
git clone https://github.com/yourusername/StockDashboard.git
cd StockDashboard
pip install -r requirements.txt
streamlit run app.py
