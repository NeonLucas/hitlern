import tkinter as tk
from PIL import Image, ImageTk
import mysql_c
import time

#debug
def testing():
	global tablenumber
	print("====> indexval is ====>", indexvals)
	print("====> tablenum is ====>", tablenumber)
	print("====> order_sn is ====>", order_list)


#global variables
#checks if order has already been done for this table
ordered = False
tablenumber = 0
order_list = []
new_orderlist = {}
menu_table = []
indexvals = [1,2,3,4,5,6]

#################PRE PROGRAMS#################
#table number assignment
def tablenumassign():
	global tablenumber
	assign = tk.Tk()
	assign.geometry("500x400")

	def assignnum():
		global tablenumber
		tablenumber = str(e1.get())
		time.sleep(0.5)
		assign.destroy()

	l1 = tk.Label(assign, text = "Please Enter Your Table Number", font = ("marck script", 25))
	e1 = tk.Entry(assign)
	b1 = tk.Button(assign, text = "ENTER", height = 2, width = 13, command = assignnum)
	l1.place(x = 25, y = 50)
	e1.place(x = 185, y = 200)
	b1.place(x = 200, y = 325)
	assign.mainloop()

#################MAIN GLOBAL VALS UPDATION FUNCTIONS#################

#ADD food to the order of customer(orderbuttons on the right)
def order1():
	global indexvals, order_list

	if menu_table[indexvals[0]-1][1] == "-":
		pass
	else:
		order_list.append(menu_table[indexvals[0]-1][0:3])

def order2():
	global indexvals, order_list
	if menu_table[indexvals[1]-1][1] == "-":
		pass
	else:
		order_list.append(menu_table[indexvals[1]-1][0:3])

def order3():
	global indexvals, order_list
	if menu_table[indexvals[2]-1][1] == "-":
		pass
	else:
		order_list.append(menu_table[indexvals[2]-1][0:3])

def order4():
	global indexvals, order_list
	if menu_table[indexvals[3]-1][1] == "-":
		pass
	else:
		order_list.append(menu_table[indexvals[3]-1][0:3])

def order5():
	global indexvals, order_list
	if menu_table[indexvals[4]-1][1] == "-":
		pass
	else:
		order_list.append(menu_table[indexvals[4]-1][0:3])

def order6():
	global indexvals, order_list
	if menu_table[indexvals[5]-1][1] == "-":
		pass
	else:
		order_list.append(menu_table[indexvals[5]-1][0:3])



#updating the inner menu_table list
def update_table_lis():
	global menu_table

	menu_table = mysql_c.select_dat(table = "menu", columns = "*")

	while len(menu_table) % 6 != 0 or len(menu_table) == 0:
		menu_table.append(("-", "-", "-"))

	#debug
	#print(menu_table)

#when order has been recieved at table
def order_recieved():
	global ordered, order_list, new_orderlist

	ordered = False
	order_list = []
	new_orderlist = {}

#################SECONDARY WINDOWS#################
#function that sends the bill in a readable manner
#(tableno, ("itemsno" + "qty", "itemsno" + "qty".....), total price)
def proceed_to_billing():
	global new_orderlist, ordered
	order_compress = ""
	summ = 0

	#the food recieved button sets this back to false
	if ordered:
		return

	for i in new_orderlist:
		summ += i[2]
		order_compress += str(i[0]) + "X" + str(new_orderlist[i]) + " "

	#adding columns to the orders table
	tnum = str(tablenumber)
	descript = order_compress
	price = summ

	columns = "(%s, \"%s\", %s)" % (tnum, descript , price)
	mysql_c.insert_val("orders", "(tablenum, descript, price)", columns)

	

	ordered = True

def show_order_box():
	global order_list, new_orderlist

	#new orderlist contains details of all food and its quantity
	new_orderlist = {}

	for i in order_list:
		new_orderlist[i] = new_orderlist.get(i, 0) + 1

	#formats how the order looks and stuff	
	def format_order(food):
		display = ""
		total = 0#what does this do again?
		summ = 0
		#title
		line = "Description".ljust(20) + "qty".ljust(5) +"rate".ljust(6)+ "price" + "\n"
		display += line

		#main part
		for i in food:
			line = ""
			summ += i[2] * food[i]

			line += i[1]
			#food[i] gives the qty by referencing to the dictionary
			line = line.ljust(20) + str(food[i]).ljust(5) +str(i[2]).ljust(6)+ str(i[2]*food[i]) + "\n"

			display += line

		##ADDING THE TOTAL SUM COST TO THE BOTTOM##

		line = "SUB TOTAL:"
		line = line.ljust(31) + str(summ) 
		display += line + "\n"

		display += "\n"

		sgst = round(((9/100) * summ),2)
		cgst = round(((9/100) * summ),2)

		line = "CGST@9%"
		line = line.ljust(31) + str(cgst)
		display += line + "\n"
		summ += cgst

		line = "SGST@9%"
		line = line.ljust(31) + str(sgst)
		display += line + "\n"
		summ += sgst
		
		display += "\n"

		line = "GRAND TOTAL"
		line = line.ljust(31) + str(round(summ,2))
		display += line

		return display


	orders_box = tk.Tk()
	orders_box.geometry("400x600")

	order_label = tk.Label(orders_box, text = format_order(new_orderlist), justify = "left", font = ("courier", 11))
	checkout_button = tk.Button(orders_box, text = "PROCEED TO BILLING", height = 2, width = 16, command = proceed_to_billing)

	order_label.pack()
	checkout_button.place(x = 150, y = 540)

	orders_box.mainloop()




#################MAIN TABLE FUNCTIONS#################
#clear whole table
def clear_screen():
	slabel1.destroy()
	slabel2.destroy()
	slabel3.destroy()
	slabel4.destroy()
	slabel5.destroy()
	slabel6.destroy()

	flabel1.destroy()
	flabel2.destroy()
	flabel3.destroy()
	flabel4.destroy()
	flabel5.destroy()
	flabel6.destroy()
	
	plabel1.destroy()
	plabel2.destroy()
	plabel3.destroy()
	plabel4.destroy()
	plabel5.destroy()
	plabel6.destroy()

#add everything to table
def screen_update():
	global indexvals, slabel1, slabel2, slabel3, slabel4, slabel5, slabel6
	global flabel1, flabel2, flabel3, flabel4, flabel5, flabel6
	global plabel1, plabel2, plabel3, plabel4, plabel5, plabel6
	
	#sno labels
	slabel1 = tk.Label(cnv,text = str(menu_table[indexvals[0]-1][0]), font = ("marck script", 22))
	slabel2 = tk.Label(cnv,text = str(menu_table[indexvals[1]-1][0]), font = ("marck script", 22))
	slabel3 = tk.Label(cnv,text = str(menu_table[indexvals[2]-1][0]), font = ("marck script", 22))
	slabel4 = tk.Label(cnv,text = str(menu_table[indexvals[3]-1][0]), font = ("marck script", 22))
	slabel5 = tk.Label(cnv,text = str(menu_table[indexvals[4]-1][0]), font = ("marck script", 22))
	slabel6 = tk.Label(cnv,text = str(menu_table[indexvals[5]-1][0]), font = ("marck script", 22))

	#food labels
	flabel1 = tk.Label(cnv,text = str(menu_table[indexvals[0]-1][1]), font = ("marck script", 22))
	flabel2 = tk.Label(cnv,text = str(menu_table[indexvals[1]-1][1]), font = ("marck script", 22))
	flabel3 = tk.Label(cnv,text = str(menu_table[indexvals[2]-1][1]), font = ("marck script", 22))
	flabel4 = tk.Label(cnv,text = str(menu_table[indexvals[3]-1][1]), font = ("marck script", 22))
	flabel5 = tk.Label(cnv,text = str(menu_table[indexvals[4]-1][1]), font = ("marck script", 22))
	flabel6 = tk.Label(cnv,text = str(menu_table[indexvals[5]-1][1]), font = ("marck script", 22))

	#price labels
	plabel1 = tk.Label(cnv,text = str(menu_table[indexvals[0]-1][2]), font = ("marck script", 22))
	plabel2 = tk.Label(cnv,text = str(menu_table[indexvals[1]-1][2]), font = ("marck script", 22))
	plabel3 = tk.Label(cnv,text = str(menu_table[indexvals[2]-1][2]), font = ("marck script", 22))
	plabel4 = tk.Label(cnv,text = str(menu_table[indexvals[3]-1][2]), font = ("marck script", 22))
	plabel5 = tk.Label(cnv,text = str(menu_table[indexvals[4]-1][2]), font = ("marck script", 22))
	plabel6 = tk.Label(cnv,text = str(menu_table[indexvals[5]-1][2]), font = ("marck script", 22))

	slabel1.place(x = 9 , y = 1*60 - 14)
	slabel2.place(x = 9, y = 2*60 - 14)
	slabel3.place(x = 9, y = 3*60 - 14)
	slabel4.place(x = 9, y = 4*60 - 14)
	slabel5.place(x = 9, y = 5*60 - 14)
	slabel6.place(x = 9, y = 6*60 - 14)
	

	flabel1.place(x = 54, y = 1*60 - 14)
	flabel2.place(x = 54, y = 2*60 - 14)
	flabel3.place(x = 54, y = 3*60 - 14)
	flabel4.place(x = 54, y = 4*60 - 14)
	flabel5.place(x = 54, y = 5*60 - 14)
	flabel6.place(x = 54, y = 6*60 - 14)
	
	plabel1.place(x = 650, y = 1*60 - 14)
	plabel2.place(x = 650, y = 2*60 - 14)
	plabel3.place(x = 650, y = 3*60 - 14)
	plabel4.place(x = 650, y = 4*60 - 14)
	plabel5.place(x = 650, y = 5*60 - 14)
	plabel6.place(x = 650, y = 6*60 - 14)

#database connectivity
mysql_c.init_connection(host = "localhost", user = "root", passwd = "sachu123", database = "hitlern")

def next_box():# give an upper limit to these poor numbers, make it so that it deletes previous labels
	global indexvals

	if indexvals[5] == len(menu_table):#at this point the numbers start peepin outta their boxes
		return

	for i in range(len(indexvals)):
		indexvals[i] = indexvals[i] + 6

	clear_screen()
	screen_update()

def prev_box():
	global indexvals

	if indexvals[0] == 1:#if the first element is 1 dont even let it be reduced any more
		return

	for i in range(len(indexvals)):
		indexvals[i] = indexvals[i] - 6

	clear_screen()
	screen_update()


#function buttons
def refresh_cmd():
	update_table_lis()
	clear_screen()
	screen_update()

#######################pre program####################### 
tablenumassign()





#window and widget creation

win = tk.Tk()
win.geometry("1080x540")

cnv = tk.Canvas(win, height= 400, width = 800)
tablenumber_label = tk.Label(win, text = "Table No." + str(tablenumber), font = ("marck script", 25))
next_button = tk.Button(win, text = "NEXT", height = 2, width = 10, command = next_box) 
prev_button = tk.Button(win, text = "PREV", height = 2, width = 10, command = prev_box)
order_rec_button = tk.Button(win, text = "RECIEVED", height = 2, width = 13, command = order_recieved)
order1_button = tk.Button(win, text = "ADD TO ORDER", height = 2, width = 13, command = order1)
order2_button = tk.Button(win, text = "ADD TO ORDER", height = 2, width = 13, command = order2)
order3_button = tk.Button(win, text = "ADD TO ORDER", height = 2, width = 13, command = order3)
order4_button = tk.Button(win, text = "ADD TO ORDER", height = 2, width = 13, command = order4)
order5_button = tk.Button(win, text = "ADD TO ORDER", height = 2, width = 13, command = order5)
order6_button = tk.Button(win, text = "ADD TO ORDER", height = 2, width = 13, command = order6)
show_order = tk.Button(win, text = "SHOW ORDER", height = 2, width = 13, command = show_order_box)
refresh = tk.Button(win, text = "REFRESH", height = 2, width = 13, command = refresh_cmd)


#function creation
def table_form_creation():
	global indexvals
	#borders
	top_horiz = cnv.create_rectangle(0, 0, 800, 5, fill = "black") #(x1, y1, x2, y2) these are actually only 4 pixels high
	left_vert = cnv.create_rectangle(0, 0, 5, 400, fill = "black")
	right_vert = cnv.create_rectangle(797, 0, 800, 400, fill = "black")#these things are plain weird
	bot_horiz = cnv.create_rectangle(0, 397, 800, 400, fill = "black")

	#margins
	left_margin = cnv.create_rectangle(40, 0, 43, 400, fill = "black")
	top_margin = cnv.create_rectangle(0, 40, 800, 43, fill = "black")

	screen_update()	

	#partitions
	pratition = cnv.create_line(640, 0, 640, 400)
	l1 = cnv.create_line(0,100,800,100)
	l2 = cnv.create_line(0,160,800,160)
	l3 = cnv.create_line(0,220,800,220)
	l4 = cnv.create_line(0,280,800,280)
	l5 = cnv.create_line(0,340,800,340)

	#labels
	sno = tk.Label(cnv, text = "s.no", font = ("marck script", 16))
	food = tk.Label(cnv, text = "Food", font = ("marck script", 16))
	price = tk.Label(cnv, text = "Price", font = ("marck script", 16))

	sno.place(x = 6, y = 6)
	food.place(x = 322, y = 6)
	price.place(x=641+50, y = 6)

update_table_lis()
table_form_creation()

tablenumber_label.place(x = 910, y = 35)
next_button.place(x = 600, y = 55)
prev_button.place(x = 540-140, y = 55)
order_rec_button.place(x = 20, y = 139)
show_order.place(x = 20, y = 139 + 70)
refresh.place(x = 20, y = 139 + 210)
cnv.place(x = 139, y = 139)

#placing order buttons
order1_button.place(x = 960, y = 188)
order2_button.place(x = 960, y = 188+60)
order3_button.place(x = 960, y = 188+(60*2))
order4_button.place(x = 960, y = 188+(60*3))
order5_button.place(x = 960, y = 188+(60*4))
order6_button.place(x = 960, y = 188+(60*5))

win.mainloop()




