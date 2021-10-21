import mysql.connector

mydb=mysql.connector.connect(
		user='devgup',
		password='devlop678',
		host='localhost',
		database='rentApp'
	)
mycursor=mydb.cursor()
#mycursor.execute('drop table rents')
#mycursor.execute('create table rents(id int not null primary key auto_increment,renter varchar(50) not null,rentee varchar(50),address varchar(50),status varchar(50) default \'available\')')
mycursor.execute('select * from rents')
myresult=mycursor.fetchall()
for x in myresult:
	print(x)