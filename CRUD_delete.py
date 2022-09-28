import mysql.connector
mysqldb=mysql.connector.connect(host="localhost",user="root",password="Alfa@123",database="pivottrading")#established connection between your database
mycursor=mysqldb.cursor()#cursor() method create a cursor object
mycursor.execute("TRUNCATE TABLE details")#Execute SQL Query to detete a record
mysqldb.commit() # Commit is used for your changes in the database
print('deteted successfully...')
# rollback used for if any error
mysqldb.rollback()
mysqldb.close()#Connection Close
