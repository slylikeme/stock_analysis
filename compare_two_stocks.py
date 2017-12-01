from bokeh.layouts import column
from bokeh.plotting import figure, show, output_file
from pandas_datareader import data
import datetime

"""
Script that uses pandas_datareader library to pull stock price information from Yahoo! Finance,
    then plots it to a candlestick chart using bokeh.plotting. This script compares Google and Apple.
"""

# stock comparison dates
start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2017, 1, 1)

# continually tries to pull data from yahoo until it is successful
while True:
    try:
        # Google dataframe
        df1 = data.DataReader(name="GOOG", data_source='yahoo', start=start, end=end)
        # Apple dataframe
        df2 = data.DataReader(name="AAPL", data_source='yahoo', start=start, end=end)
    except RemoteDataError:
        continue
    break

# convert hours to milliseconds to use datetime
hours_12 = 12 * 60 * 60 * 1000

# function to add status column
def inc_dec(c, o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "Equal"
    return value

# Add new columns to google dataframe
df1["Status"] = [inc_dec(c, o) for c, o in zip(df1.Close, df1.Open)]
df1["Middle"] = (df1.Open + df1.Close) / 2
df1["Height"] = abs(df1.Close - df1.Open)

# Add new columns to apple dataframe
df2["Status"] = [inc_dec(c, o) for c, o in zip(df2.Close, df2.Open)]
df2["Middle"] = (df2.Open + df2.Close) / 2
df2["Height"] = abs(df2.Close - df2.Open)

# Create google candlestick plot
s1 = figure(x_axis_type='datetime', width=1100, height=300, responsive=True)
s1.title.text = "Google Stock Performace 2016"
s1.grid.grid_line_alpha = 0.3

# segment that plots from high to low point
s1.segment(df1.index, df1.High, df1.index, df1.Low, color="black")

# rectangles that plot open and closing, and color depending on if the day was a net loss or net gain
s1.rect(df1.index[df1.Status == "Increase"], df1.Middle[df1.Status == "Increase"], hours_12,
        df1.Height[df1.Status == "Increase"], fill_color="#228B22", line_color="black")
s1.rect(df1.index[df1.Status == "Decrease"], df1.Middle[df1.Status == "Decrease"], hours_12,
        df1.Height[df1.Status == "Decrease"], fill_color="#F08080", line_color="black")

# Create apple candlestick plot
s2 = figure(x_axis_type='datetime', width=1100, height=300, responsive=True)
s2.title.text = "Apple Stock Performace 2016"
s2.grid.grid_line_alpha = 0.3

# segment that plots from high to low point
s2.segment(df2.index, df2.High, df2.index, df2.Low, color="black")

# rectangles that plot open and closing, and color depending on if the day was a net loss or net gain
s2.rect(df2.index[df2.Status == "Increase"], df2.Middle[df2.Status == "Increase"], hours_12,
        df2.Height[df2.Status == "Increase"], fill_color="#228B22", line_color="black")
s2.rect(df2.index[df2.Status == "Decrease"], df2.Middle[df2.Status == "Decrease"], hours_12,
        df2.Height[df2.Status == "Decrease"], fill_color="#F08080", line_color="black")

# put plots into column on single html page
p = column(s1, s2)

# write to html file
output_file("GoogleVsAppleStock.html")

# display html file
show(p)
