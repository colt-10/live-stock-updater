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
import mysql.connector
mysqldb=mysql.connector.connect(host="localhost",user="root",password="Alfa@123",database="pivottrading")#established connection between your database
mycursor=mysqldb.cursor()#cursor() method create a cursor object
#Execute SQL Query to insert record
mycursor.execute( """insert into trade(Scrip,`Prev High`,`Prev Low`,LTP,Timing,Result)
values (%s,%s,%s,%s,%s,%s)on duplicate key update
Scrip=%s,
`Prev High`=%s,
`Prev Low` =%s,
LTP=%s,
Timing=%s,
Result=%s """,df)
mysqldb.commit() # Commit is used for your changes in the database
print('Record inserted successfully...')
# rollback used for if any errorS
mysqldb.rollback()
mysqldb.close()#Connection Close



