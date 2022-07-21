import yfinance as yf
import streamlit as st

st.title("Simple Stock Price App")
tickers = ['GME', 'AAPL', 'MSFT', 'GOOG', 'NFLX', 'AMZN']
ticker_selected = st.selectbox("Select a ticker", tickers)
tickerData = yf.Ticker(ticker_selected)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2015-5-31', end='2022-5-31')

st.subheader("Close Price")
st.line_chart(tickerDf.Close)
st.subheader("Volume")
st.line_chart(tickerDf.Volume)
st.subheader("Institutional Holders")
st.write(tickerData.institutional_holders)

with st.expander("View Stock Wiki", expanded=False):
    st.write(tickerData.info)
