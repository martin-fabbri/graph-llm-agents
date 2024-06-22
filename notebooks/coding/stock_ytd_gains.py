# filename: stock_ytd_gains.py

import yfinance as yf
import datetime
import matplotlib.pyplot as plt

# Define the stock tickers and start date (beginning of the year)
tickers = ['NVDA', 'TSLA']
start_date = '2024-01-01'
end_date = '2024-06-21'

# Fetch the stock data from Yahoo Finance
nvda_data = yf.download('NVDA', start=start_date, end=end_date)
tsla_data = yf.download('TSLA', start=start_date, end=end_date)

# Calculate the YTD gains
nvda_data['YTD_Gain'] = (nvda_data['Close'] / nvda_data['Close'][0] - 1) * 100
tsla_data['YTD_Gain'] = (tsla_data['Close'] / tsla_data['Close'][0] - 1) * 100

# Plot the YTD gains
plt.figure(figsize=(10, 6))
plt.plot(nvda_data.index, nvda_data['YTD_Gain'], label='NVDA')
plt.plot(tsla_data.index, tsla_data['YTD_Gain'], label='TSLA')
plt.xlabel('Date')
plt.ylabel('YTD Gain (%)')
plt.title('Year-to-Date (YTD) Gain for NVDA and TSLA')
plt.legend()
plt.grid(True)
plt.savefig('ytd_stock_gains.png')
plt.show()