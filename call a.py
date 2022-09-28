import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
url =  ("https://www.pivottrading.co.in/beta/tools/prb-scanner-equity.php?broker=fyers")
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
df =pd.DataFrame(rows[:-1],columns=headers[1:])
pd.set_option('expand_frame_repr', False)
print(df)
#pip install pymysql
import pymysql
#Save data to the table
conn = pymysql.connect(host='localhost',user='root',password='Alfa@123',database='pivottrading')
query = """insert into trade(Scrip,`Prev High`,`Prev Low`,LTP,Timing,Result)
values (%s,%s,%s,%s,%s,%s)on duplicate key update
Scrip=%s,
`Prev High`=%s,
`Prev Low` =%s,
LTP=%s,
Timing=%s,
Result=%s """
records_to_insert = df
cursor = conn.cursor()
cursor.executemany(query,records_to_insert)
conn.commit()
print(cursor.rowcount, "Record inserted successfully into trade table")
# disconnect from server
conn.close()
print('done')