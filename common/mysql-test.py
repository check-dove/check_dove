import mysql.connector

con = mysql.connector.connect(
    host='localhost', port=3306,
    user='root', password='jianshemima66',
)
con.close()
