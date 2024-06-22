# filename: download_and_plot_stocks.py
from functions import get_stock_prices, plot_stock_prices
import datetime

# Define the start and end dates
start_date = '2024-01-01'
end_date = '2024-06-21'

# Define stock symbols
stock_symbols = ['NVDA', 'TSLA']

# Get the stock prices
stock_prices = get_stock_prices(stock_symbols, start_date, end_date)

# Plot the stock prices and save to file
plot_stock_prices(stock_prices, 'stock_prices_YTD_plot.png')

# Print confirmation
print("Stock prices plotted and saved to stock_prices_YTD_plot.png")