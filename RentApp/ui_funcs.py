import tkinter as tk
from sql_funcs import *

session_user=str(input('username:'))

def show_avl_houses():
	def make_booking():
		book_house(avl_houses_selection.get(),session_user)

	avl_houses_win=tk.Toplevel()
	avl_houses_selection=tk.StringVar()
	avl_houses=show_houses()
	n=1
	tk.Label(avl_houses_win,text='renter\trentee\taddress').grid(row=0,column=0)
	for x in avl_houses:
		tk.Radiobutton(avl_houses_win,text=str(str(x[1])+'\t'+str(x[2])+'\t'+str(x[3])),value=x[0],variable=avl_houses_selection).grid(row=n,column=0)
		n+=1
	tk.Button(avl_houses_win,text='Book',command=make_booking).grid(row=n,column=0)
	avl_houses_win.mainloop()

def show_history():
	show_history_win=tk.Toplevel()
	history_values=user_history(session_user)
	n=1
	tk.Label(show_history_win,text='Renter\tRentee\tAddress\tStatus').grid(row=0,column=0)
	for x in history_values:
		tk.Label(show_history_win,text=str(str(x[1])+'\t'+str(x[2])+'\t'+str(x[3])+'\t'+str(x[4]))).grid(row=n,column=0)
		n+=1
	show_history_win.mainloop()

def pending_requests():
	pending_requests_win=tk.Toplevel()
	pending_requests_values=renter_pending_houses(session_user)
	pending_requests_var=tk.IntVar()
	n=1
	tk.Label(pending_requests_win,text='Rentee\tAddress').grid(row=0,column=0)
	for x in pending_requests_values:
		tk.Label(pending_requests_win,text=str(str(x[2])+'\t'+str(x[3]))).grid(row=n,column=0)
		tk.Button(pending_requests_win,text='Accept',command=lambda:confirm_request(x[0])).grid(row=n,column=1)
		tk.Button(pending_requests_win,text='Reject',command=lambda:reject_request(x[0])).grid(row=n,column=2)
		n+=1
	pending_requests_win.mainloop()

def current_rented():
	current_rented_win=tk.Toplevel()
	current_rented_values=current_rented_houses(session_user)
	current_rented_var=tk.IntVar()
	n=1
	tk.Label(current_rented_win,text='Renter\tRentee\tAddress').grid(row=0,column=0)
	for x in current_rented_values:
		tk.Label(current_rented_win,text=str(str(x[1])+'\t'+str(x[2])+'\t'+str(x[3]))).grid(row=n,column=0)
		tk.Button(current_rented_win,text='Delete',command=lambda:unrent_house(x[0])).grid(row=n,column=1)
		tk.Button(current_rented_win,text='Unoccupy',command=reject_request(x[0])).grid(row=n,column=2)
		n+=1
	current_rented_win.mainloop()

def user_booked_houses():
	user_booked_houses_win=tk.Toplevel()
	user_booked_values=booked_houses(session_user)
	n=1
	tk.Label(user_booked_houses_win,text='Renter\tRentee\tAddress\tStatus').grid(row=0,column=0)
	for x in user_booked_values:
		tk.Label(user_booked_houses_win,text=str(str(x[1])+'\t'+str(x[2])+'\t'+str(x[3])+'\t'+str(x[4]))).grid(row=n,column=0)
		n+=1
	user_booked_houses_win.mainloop()

def ui_rent_house():
	rent_house_win=tk.Toplevel()
	adr=tk.StringVar()
	def rent_house_sql():
		rent_house(session_user,adr.get())
	tk.Label(rent_house_win,text='Address:').grid(row=0,column=0)
	address=tk.Entry(rent_house_win,textvariable=adr).grid(row=0,column=1)
	tk.Button(rent_house_win,text='Rent',command=rent_house_sql).grid(row=1,column=0)
	rent_house_win.mainloop()