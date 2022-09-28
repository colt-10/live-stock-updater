import pandas as pd
import pymysql
# Connect to the database
connection = pymysql.connect(host='localhost',
                         user='root',
                         password='Alfa@123',
                         db='pivottrading')
# create cursor
cursor=connection.cursor()
# Create dataframe
data = pd.DataFrame({ "Scrip"   : ['OLX','MSFT','APPL','TESLA'],
                      "P.Close": ['456','567','876','900'],
                      "Open" : ['567','765','908','500'],
                      "High": [ '100','200','478','890'],
                      "Low":['657','890','765','453'],
                      "LTP@REAL":['567','897','675','683'],
                      "LTP(NOW)":['594','786','873','838'],
                      "Result":['0','0','0','0']})
# creating column list for insertion
cols = "`,`".join([str(i) for i in data.columns.tolist()])

# Insert DataFrame recrds one by one.
for i,row in data.iterrows():
    sql = "INSERT INTO `details` (`" + cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    cursor.execute(sql,tuple(row))

    # the connection is not autocommitted by default, so we must commit to save our changes
    connection.commit()
    # Execute query
    sql = "SELECT * FROM `details`"
    cursor.execute(sql)

    # Fetch all the records
    result = cursor.fetchall()
    for i in result:
        print(i)