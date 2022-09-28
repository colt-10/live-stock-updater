import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                         database='pivottrading',
                                         user='root',
                                         password='Alfa@123')
cursor = connection.cursor()
cursor.callproc('sp_trade',['aa', '900', '98', '345', '89', '345'])
# print results
print("Printing")
for result in cursor.stored_results():
    print(result.fetchall())
if (connection.is_connected()):
    cursor.close()
    connection.close()
    print("MySQL connection is closed")

