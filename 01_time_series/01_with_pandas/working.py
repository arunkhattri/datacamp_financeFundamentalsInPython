"Working with Time Series in Pandas"

import pandas as pd
import numpy as np
from datetime import datetime
import yfinance as yf
import mplfinance as mpf

# Basic building block: pd.Timestamp
time_stamp = pd.Timestamp(datetime(2023, 3, 29))
print(time_stamp)

pd.Timestamp("2023-03-29") == time_stamp

msg = f"both are not the same thing."
assert pd.Timestamp("2023-03-29") == time_stamp, msg

# attributes
print(time_stamp.year)
print(time_stamp.day_name())

# Sequence of dates & times
index = pd.date_range(start="2022-01-01", periods=12, freq="M")
print(index)

print(index[0])

# timestamp to period
print(index.to_period())

# pandas dataframe with timestamp
data = np.random.rand(12, 2)

df = pd.DataFrame(index=index, data=data)
df.info()

# Exercises
seven_days = pd.date_range(start="2023-1-1", freq="D", periods=7)

for day in seven_days:
    print(day.dayofweek, day.day_name())

# Time series transformation
goog = yf.Ticker("GOOG")
goog_data = goog.history(start="2022-03-01", end="2023-03-28", actions=False)
print(goog_data.head())

# plotting close price, ohlc chart
# left mark - open, right mark - close
mpf.plot(goog_data)


# slicing and indexing
google_jan_onwards = goog_data["2023-1":"2023-3"]
google_jan_onwards.info()

mpf.plot(google_jan_onwards, type="candle")
