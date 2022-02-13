import mysql.connector

mydb=mysql.connector.connect(
		user='devgup',  #username
		password='devlop678',   #password
		host='localhost',
	)
mycursor=mydb.cursor()

mycursor.execute('create database rentApp')
mydb.commit()
mycursor.execute('use rentApp')
mycursor.execute('create table rents(id int not null primary key auto_increment,renter varchar(50) not null,rentee varchar(50),address varchar(50),status varchar(50) default \'available\')')
mycursor.execute("insert into rents(renter,address) values('Sam','adr1')")
mycursor.execute("insert into rents(renter,address) values('Tom','adr2')")
mycursor.execute("insert into rents(renter,address) values('John','adr3')")
mycursor.execute("insert into rents(renter,address) values('John','adr4')")
mycursor.execute("insert into rents(renter,address) values('Sam','adr5')")
mycursor.execute("insert into rents(renter,address) values('Toby','adr6')")
mycursor.execute("insert into rents(renter,address) values('Bill','adr7')")
mycursor.execute("insert into rents(renter,address) values('Sam','adr8')")
mycursor.execute("insert into rents(renter,address) values('Alex','adr9')")
mycursor.execute("insert into rents(renter,address) values('John','adr10')")
mycursor.execute("insert into rents(renter,address) values('Toby','adr11')")
mycursor.execute("insert into rents(renter,address) values('Dave','adr12')")
mydb.commit()
mycursor.execute('select * from rents')
myresult=mycursor.fetchall()
for x in myresult:
	print(x)
