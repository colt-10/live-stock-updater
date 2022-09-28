import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
url =  ("https://www.pivottrading.co.in/beta/tools/open-high-low-scanner.php?broker=zerodha#")
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
table = soup.find('table', {'class' : 'table'})
rows = table.find_all('th')
headers = []
for i in table.find_all('th'):
    title = i.text
    headers.append(title)
rows=[]
for row in table.find_all('tr')[1:]:
        data = row.find_all('td')
        rows.append(td.text.strip()for td in data[1:])
df=pd.DataFrame(rows[:-1],columns=headers[1:])
pd.set_option('expand_frame_repr', False)
print(df)
engine = create_engine('mysql+pymysql://root:Alfa@123@localhost:3306/pivottrading')
data = pd.DataFrame(df)
data.to_sql('details', con = engine, if_exists = 'append', chunksize = 1000,index = False)
print('Done')

