import mysql.connector #Importing Connector package
mysqldb=mysql.connector.connect(host="localhost",user="root",password="")#established connection
mycursor=mysqldb.cursor()#cursor() method create a cursor object
mycursor.execute("create database dbpython")#Execute SQL Query to create a database
mysqldb.close()#Connection Close

