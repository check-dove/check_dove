import pymysql

# database为逻辑空间
connection = pymysql.connect(host='localhost', user='root', password='jianshemima66',
                             database='demo', port=3306, charset='UTF8')
cur = connection.cursor()

delimiter = "="*100
version = "select version();"
selectall = "SELECT * from t_dept;"


print(delimiter)

cur.execute(version)
data = cur.fetchone()
print('database version:', data)


print(delimiter)
cur.execute(selectall)
all_data = cur.fetchall()
for i in all_data:
    print(i)


cur.scroll(1, mode='absolute')
data1 = cur.fetchone()
print(data1)


cur.scroll(-2, mode='relative')
data2 = cur.fetchone()
print(data2)


cur.close()
connection.close()
