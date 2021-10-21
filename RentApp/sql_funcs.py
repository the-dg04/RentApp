import mysql.connector

mydb=mysql.connector.connect(
		user='devgup',
		password='devlop678',
		host='localhost',
		database='rentApp'
	)
mycursor=mydb.cursor()

def rent_house(renter,address):
	return_str='insert into rents(renter,address) values(\''+str(renter)+'\',\''+str(address)+'\')'
	mycursor.execute(return_str)
	mydb.commit()
	print(mycursor)

def show_houses():
	lst=[]
	mycursor.execute('select * from rents where status=\'available\'')
	myresult=mycursor.fetchall()
	for x in myresult:
		lst+=[x]
	return(lst)

def book_house(idx,rentee):
	return_str='update rents set rentee=\''+str(rentee)+'\',status=\'pending\' where id=\''+str(idx)+'\''
	mycursor.execute(return_str)
	mydb.commit()

def confirm_request(idx):
	return_str='update rents set status=\'booked\' where id=\''+str(idx)+'\''
	mycursor.execute(return_str)
	mydb.commit()

def reject_request(idx):
	return_str='update rents set status=\'available\',rentee=null where id=\''+str(idx)+'\''
	mycursor.execute(return_str)
	mydb.commit()

def unrent_house(idx):
	return_str='update rents set status=\'unavailable\' where id=\''+str(idx)+'\''
	mycursor.execute(return_str)
	mydb.commit()

def user_rented_houses(renter):
	lst=[]
	mycursor.execute('select * from rents where renter=\''+str(renter)+'\'')
	myresult=mycursor.fetchall()
	for x in myresult:
		lst+=[x]
	return(lst)

def user_rentee_houses(rentee):
	lst=[]
	mycursor.execute('select * from rents where rentee=\''+str(rentee)+'\'')
	myresult=mycursor.fetchall()
	for x in myresult:
		lst+=[x]
	return(lst)

def renter_pending_houses(renter):
	lst=[]
	mycursor.execute('select * from rents where renter=\''+str(renter)+'\' AND status=\'pending\'')
	myresult=mycursor.fetchall()
	for x in myresult:
		lst+=[x]
	return(lst)

def rentee_pending_houses(rentee):
	lst=[]
	mycursor.execute('select * from rents where renter=\''+str(rentee)+'\',status=\'pending\'')
	myresult=mycursor.fetchall()
	for x in myresult:
		lst+=[x]
	return(lst)

def user_history(user):
	lst=[]
	mycursor.execute('select * from rents where renter=\''+str(user)+'\'')
	myresult=mycursor.fetchall()
	for x in myresult:
		lst+=[x]
	mycursor.execute('select * from rents where rentee=\''+str(user)+'\'')
	myresult=mycursor.fetchall()
	for x in myresult:
		lst+=[x]
	return(lst)

#rent_house('dhruv','adr2')

def current_rented_houses(renter):
	lst=[]
	mycursor.execute('select * from rents where renter=\''+str(renter)+'\'')
	myresult=mycursor.fetchall()
	for x in myresult:
		if x[4]=='booked':
			lst+=[x]
	return(lst)
#print(current_rented_houses('dhruv'))

def booked_houses(rentee):
	lst=[]
	mycursor.execute('select * from rents where rentee=\''+str(rentee)+'\'')
	myresult=mycursor.fetchall()
	for x in myresult:
		if x[4]=='booked':
			lst+=[x]
	return(lst)