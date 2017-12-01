# stock_analysis

![ScreenShot](.\images\stock_analysis_example.png)

Creates candlestick graph tracking stock prices over a given time frame.

Pulls data from Yahoo! Finance using pandas_datareader. This can be configured to use Google Finance if desired.

User can change which company is tracked by updating: name="GOOG" in data.Datareader.

Uses bokeh.plotting to create the candlestick graph.

Uses datetime to plot stock prices(Open, Close, High, Low) along the x-axis.

Days with positive gains are shown in green. Days with negative gains are shown in red.

High and low prices are displayed as black segment line.