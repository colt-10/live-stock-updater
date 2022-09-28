import mysql.connector
import pandas as pd
mysqldb=mysql.connector.connect(host="localhost",user="root",password="Alfa@123",database="sportsperson")#established connection between your database
mycursor=mysqldb.cursor()#cursor() method create a cursor object
mycursor.execute("UPDATE details SET name='adam', age=21 WHERE id=3")#Execute SQL Query to update record
mysqldb.commit() # Commit is used for your changes in the database
print('updated successfully...')
# rollback used for if any error
mysqldb.rollback()
mysqldb.close()#Connection Close
