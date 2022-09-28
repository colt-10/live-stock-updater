import pandas_datareader as pdr
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
df = pdr.get_data_yahoo('MSFT',dt.datetime(2021,1,1,),dt.datetime.now())
df.index = df.index.date
pd.set_option('expand_frame_repr', False)
delta = df['Close'].diff()
up=delta.clip(lower=0)
down=-1*delta.clip(upper=0)
ema_up = up.ewm(com=13,adjust=False).mean()
ema_down = down.ewm(com=13,adjust=False).mean()
rs = ema_up/ema_down
df['RSI'] = 100-(100/1+rs)
print(df.tail())
pd.set_option('expand_frame_repr',False)
df = pdr.get_data_yahoo('MSFT',dt.datetime(2021,1,1,),dt.datetime.now())
df['14-low'] = df['Low'].rolling(14).min()
df['14-high'] = df['High'].rolling(14).max()
df['%k'] = ((df['Close']-df['14-low'])/(df['14-high']-df['14-low']))
df['%d'] = df['%k'].rolling(3).mean()
print(df.tail())
ax =df[['%k','%d']].plot()
df['Close'].plot(ax=ax,secondary_y=True)
ax.axhline(20,linestyle='--',color='green')
ax.axhline(80,linestyle='--',color='green')
print(plt.show())
