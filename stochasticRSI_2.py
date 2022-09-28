# ___library_import_statements___
import pandas as pd
# for pandas_datareader, otherwise it might have issues, sometimes there is some version mismatch
pd.core.common.is_list_like = pd.api.types.is_list_like
# make pandas to print dataframes nicely
pd.set_option('expand_frame_repr', False)
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime as dt
import time
#newest yahoo API
import yfinance as yahoo_finance
#optional
#yahoo_finance.pdr_override()
# ___variables___
ticker = 'MSFT'
start_time = dt.datetime(2021, 1, 1)
#end_time = datetime.datetime(2019, 1, 20)
end_time = dt.datetime.now().date().isoformat()         # today
connected = False
while not connected:
    try:
        ticker_df = pdr.get_data_yahoo(ticker, start=start_time, end=end_time)
        connected = True
        print('connected to yahoo')
    except Exception as e:
        print("type error: " + str(e))
        time.sleep( 5 )
        pass
# use numerical
# integer index instead of date
#ticker_df = ticker_df.reset_index()
df= ticker_df
def computeRSI(data, time_window):
    diff = data.diff(1).dropna()  # diff in one field(one day)
    # this preservers dimensions off diff values
    up_chg = 0 * diff
    down_chg = 0 * diff
    # up change is equal to the positive difference, otherwise equal to zero
    up_chg[diff > 0] = diff[diff > 0]
    # down change is equal to negative difference, otherwise equal to zero
    down_chg[diff < 0] = diff[diff < 0]
    # check pandas documentation for ewm
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ewm.html
    # values are related to exponential decay
    # we set com=time_window-1 so we get decay alpha=1/time_window
    up_chg_avg = up_chg.ewm(com=time_window - 1, min_periods=time_window).mean()
    down_chg_avg = down_chg.ewm(com=time_window - 1, min_periods=time_window).mean()
    rs = abs(up_chg_avg / down_chg_avg)
    rsi = 100 - 100 / (1 + rs)
    return rsi
df['RSI'] = computeRSI(df['Adj Close'], 14)
def stochastic(data, k_window, d_window, window):
    # input to function is one column from df
    # containing closing price or whatever value we want to extract K and D from
    min_val = data.rolling(window=window, center=False).min()
    max_val = data.rolling(window=window, center=False).max()
    stoch = ((data - min_val) / (max_val - min_val)) * 100
    K = stoch.rolling(window=k_window, center=False).mean()
    # K = stoch
    D = K.rolling(window=d_window, center=False).mean()
    return K, D
df['K'], df['D'] = stochastic(df['RSI'], 3, 3, 14)
df.head()
print(df.head())
def plot_price(df):
    # plot price
    plt.figure(figsize=(15,5))
    plt.plot(df['Adj Close'])
    plt.title('Price chart (Adj Close)')
    plt.show()
    return None
def plot_RSI(df):
    # plot correspondingRSI values and significant levels
    plt.figure(figsize=(15,5))
    plt.title('RSI chart')
    plt.plot(df['RSI'])
    plt.axhline(0, linestyle='--', alpha=0.1)
    plt.axhline(20, linestyle='--', alpha=0.5)
    plt.axhline(30, linestyle='--')
    plt.axhline(70, linestyle='--')
    plt.axhline(80, linestyle='--', alpha=0.5)
    plt.axhline(100, linestyle='--', alpha=0.1)
    plt.show()
    return None
def plot_stoch_RSI(df):
    # plot corresponding Stoch RSI values and significant levels
    plt.figure(figsize=(15,5))
    plt.title('stochRSI chart')
    plt.plot(df['K'])
    plt.plot(df['D'])
    plt.axhline(0, linestyle='--', alpha=0.1)
    plt.axhline(20, linestyle='--', alpha=0.5)
    #plt.axhline(30, linestyle='--')
    #plt.axhline(70, linestyle='--')
    plt.axhline(80, linestyle='--', alpha=0.5)
    plt.axhline(100, linestyle='--', alpha=0.1)
    plt.show()
    return None
def plot_all(df):
    plot_price(df)
    plot_RSI(df)
    plot_stoch_RSI(df)
    return None
plot_all(df)

