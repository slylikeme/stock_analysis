# stock_analysis
Creates candlestick graph tracking stock prices over a given time frame

Pulls data from Yahoo! Finance using pandas_datareader. This can be configured to use Google Finance if desired.

User can change which company is tracked by updating: name="GOOG" in data.Datareader

Uses bokeh.plotting to create the candlestick graph

Uses datetime to plot stock prices(Open, Close, High, Low) along the x-axis