import pymysql
connection=pymysql.connect(user="root",host="127.0.0.1",db="summer")
print("conection established")
mycursor=connection.cursor()
'''
que="create table login_info (username varchar(30), password varchar (10))"
mycursor.execute(que)
print("Table created successfully")

que1="insert into login_info(username,password) values('hum','tum')"

name=input("enter username")
password=input("enter password")
que1="insert into login_info(username,password) values(%s,%s)"
val=(name,password)
mycursor.execute(que1,val)
connection.commit()
print("Data inserted successfully")'''
fetch_data="select * from login_info"
mycursor.execute(fetch_data)
result=mycursor.fetchall()
print(result)
final_result = [list(i) for i in result]

print(final_result)
connection.close()