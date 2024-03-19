import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

# タイトルの設定
st.title('株価データの可視化アプリ')

# 銘柄の選択肢
ticker_options = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB', 'TSLA']
selected_ticker = st.selectbox('株式シンボルを選択してください', options=ticker_options)

# yfinanceで株価データを取得
ticker_data = yf.Ticker(selected_ticker)
ticker_df = ticker_data.history(period='1d', start='2010-1-1', end='2023-1-1')

# 終値のグラフを描画
close_trace = go.Scatter(x=ticker_df.index, y=ticker_df['Close'], name='終値', line=dict(color='royalblue', width=4))
data = [close_trace]
layout = go.Layout(title=f'{selected_ticker} の終値', xaxis_title='日付', yaxis_title='終値', template='plotly_dark')
fig = go.Figure(data=data, layout=layout)
st.plotly_chart(fig, use_container_width=True)

# 取引量のグラフを描画
volume_trace = go.Bar(x=ticker_df.index, y=ticker_df['Volume'], name='取引量', marker_color='orange')
data = [volume_trace]
layout = go.Layout(title=f'{selected_ticker} の取引量', xaxis_title='日付', yaxis_title='取引量', template='plotly_dark')
fig = go.Figure(data=data, layout=layout)
st.plotly_chart(fig, use_container_width=True)
