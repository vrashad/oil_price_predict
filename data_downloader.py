import yfinance as yf
from pandas_datareader import data as pdr



yf.pdr_override()
data = pdr.get_data_yahoo("CL=F", start="2000-01-01", end="2024-01-06")
selected_columns = data.iloc[:, [4]]
selected_columns.to_csv('dataset.csv')