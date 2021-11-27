import tkinter as tk
from sql_funcs import *
from ui_funcs import *

root=tk.Tk()
root.title('RentApp')
tk.Label(root,text='Welcome to RentApp!').grid(row=0,column=0)
get_house_button=tk.Button(root,text='Get House',command=show_avl_houses)
get_house_button.grid(row=1,column=0)
pending_houses_button=tk.Button(root,text='Pending requests',command=pending_requests)
pending_houses_button.grid(row=1,column=1)
my_history_button=tk.Button(root,text='History',command=show_history)
my_history_button.grid(row=2,column=0)
booked_houses=tk.Button(root,text='your booked houses',command=user_booked_houses)
booked_houses.grid(row=2,column=1)
rent_house=tk.Button(root,text='Rent house',command=ui_rent_house)
rent_house.grid(row=3,column=0)
current_rented_houses=tk.Button(root,text='current rented houses',command=current_rented)
current_rented_houses.grid(row=3,column=1)
root.mainloop()