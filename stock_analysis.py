from bokeh.plotting import figure, show, output_file
from pandas_datareader import data
import datetime

"""
Script that uses pandas_datareader library to pull stock price information from Yahoo! Finance,
    then plots it to a candlestick chart using bokeh.plotting.
    Any stock can be checked by replacing the following:
        name="GOOG"
    Simply change parameter to appropriate ticker abbreviation.
"""

# stock data dates
start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2017, 1, 1)

# continually tries to pull data from yahoo until it is successful
while True:
    try:
        df = data.DataReader(name="GOOG", data_source='yahoo', start=start, end=end)
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

# Add new columns to dataframe
df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
df["Middle"] = (df.Open + df.Close) / 2
df["Height"] = abs(df.Close - df.Open)

# Create candlestick plot
p = figure(x_axis_type='datetime', width=1000, height=300, responsive=True)
p.title.text = "Google Stock Performace 2016"
p.grid.grid_line_alpha = 0.3

# segment that plots from high to low point
p.segment(df.index, df.High, df.index, df.Low, color="black")

# rectangles that plot open and closing, and color depending on if the day was a net loss or net gain
p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], hours_12, df.Height[df.Status == "Increase"],
       fill_color="#228B22", line_color="black")
p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"], hours_12, df.Height[df.Status == "Decrease"],
       fill_color="#F08080", line_color="black")

# write to html file
output_file("GoogleStock.html")
# display html file
show(p)
