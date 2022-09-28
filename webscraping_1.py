import pandas as pd
df = pd.read_html('https://www.pivottrading.co.in/beta/tools/open-high-low-scanner.php?broker=zerodha')[0]
df.drop(columns={'Sr.No.'},inplace=True)
df.iloc[-1,0:4]=''
df.fillna(0,inplace=True)
pd.set_option('expand_frame_repr', False)
print(df)