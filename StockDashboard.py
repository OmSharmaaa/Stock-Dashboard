import streamlit as st, yfinance as yf, pandas as pd, numpy as np
import plotly.express as px
import datetime

st.title("Stock Dashboard")


ticker = st.sidebar.text_input("Ticker", value="F")

today = datetime.date.today()
default_start = today - datetime.timedelta(days=365)
start_date = st.sidebar.date_input("Start date", value=default_start)
end_date = st.sidebar.date_input("End date")

data = yf.download(ticker, start=start_date, end=end_date)
fig = px.line(data, x = data.index, y = data['Close'].squeeze(), title = ticker)
st.plotly_chart(fig)

pricing_data, fundamental_data, news = st.tabs(['Pricing Data', 'Fundamental Data', 'Top 10 NEWS'])

with pricing_data:
    st.header("Price Movements")
    data2 = data
    data2["% Change"] = data["Close"]/data["Close"].shift(1) - 1
    data2.dropna(inplace=True)
    st.write(data2)

    annual_return = data2["% Change"].mean()*252*100
    st.write("Annual Return is ", annual_return,"%")

    stdev = np.std(data["% Change"])*np.sqrt(252)
    st.write("Standard Deviation is ", stdev,"%")
    st.write("Risk Adj. Return is ", annual_return/(stdev*100))

from alpha_vantage.fundamentaldata import FundamentalData
with fundamental_data:
    key = "UFRB831D3LABC0OL"
    fd = FundamentalData(key, output_format='pandas')

    try:
        st.subheader("Balance Sheet")
        balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
        bs = balance_sheet.T[2:]
        bs.columns = list(balance_sheet.T.iloc[0])
        st.write(bs)

        st.subheader("Income Statement")
        income_statement = fd.get_income_statement_annual(ticker)[0]
        is1 = income_statement.T[2:]
        is1.columns = list(income_statement.T.iloc[0])
        st.write(is1)

        st.subheader("Cash Flow Statement")
        cash_flow = fd.get_cash_flow_annual(ticker)[0]
        cf = cash_flow.T[2:]
        cf.columns = list(cash_flow.T.iloc[0])
        st.write(cf)

    except ValueError as e:
        if "rate limit" in str(e).lower():
            st.warning("⚠️ You've hit the Alpha Vantage free API daily limit (25 requests). Please try again tomorrow or upgrade to a premium key.")
        else:
            st.error(f"❌ Failed to retrieve fundamental data: {e}")


from stocknews import StockNews
with news:
    st.header(f'News of {ticker}')
    sn = StockNews(ticker, save_news=False)
    df_news = sn.read_rss()
    for i in range(10):
        st.subheader(f'News {i+1}')
        st.write(df_news['published'][i])
        st.write(df_news['title'][i])
        st.write(df_news['summary'][i])
        title_sentiment = df_news['sentiment_title'][i]
        st.write(f'Title Sentiment {title_sentiment}')
        news_sentiment = df_news['sentiment_summary'][i]
        st.write(f'News Sentiment {news_sentiment}')