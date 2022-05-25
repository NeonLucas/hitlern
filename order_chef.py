import tkinter as tk
import mysql_c

#globals 
order_table = []
indexvals = [1,2,3,4,5,6]
mysql_c.init_connection(host = "localhost", user = "root", passwd = "sachu123", database = "hitlern")



def orders_box():
	orders = tk.Tk()
	orders.geometry("1080x540")
	
	
def update_table_lis():
	global order_table

	order_table = mysql_c.select_dat(table = "orders", columns = "*")

	while len(order_table) % 6 != 0 or len(order_table) == 0:
		order_table.append(("-", "-", "-"))

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

def screen_update():
	global indexvals, slabel1, slabel2, slabel3, slabel4, slabel5, slabel6
	global flabel1, flabel2, flabel3, flabel4, flabel5, flabel6
	global plabel1, plabel2, plabel3, plabel4, plabel5, plabel6
	
	#sno labels
	slabel1 = tk.Label(cnv,text = str(order_table[indexvals[0]-1][0]), font = ("marck script", 22))
	slabel2 = tk.Label(cnv,text = str(order_table[indexvals[1]-1][0]), font = ("marck script", 22))
	slabel3 = tk.Label(cnv,text = str(order_table[indexvals[2]-1][0]), font = ("marck script", 22))
	slabel4 = tk.Label(cnv,text = str(order_table[indexvals[3]-1][0]), font = ("marck script", 22))
	slabel5 = tk.Label(cnv,text = str(order_table[indexvals[4]-1][0]), font = ("marck script", 22))
	slabel6 = tk.Label(cnv,text = str(order_table[indexvals[5]-1][0]), font = ("marck script", 22))

	#food labels
	flabel1 = tk.Label(cnv,text = str(order_table[indexvals[0]-1][1]), font = ("marck script", 22))
	flabel2 = tk.Label(cnv,text = str(order_table[indexvals[1]-1][1]), font = ("marck script", 22))
	flabel3 = tk.Label(cnv,text = str(order_table[indexvals[2]-1][1]), font = ("marck script", 22))
	flabel4 = tk.Label(cnv,text = str(order_table[indexvals[3]-1][1]), font = ("marck script", 22))
	flabel5 = tk.Label(cnv,text = str(order_table[indexvals[4]-1][1]), font = ("marck script", 22))
	flabel6 = tk.Label(cnv,text = str(order_table[indexvals[5]-1][1]), font = ("marck script", 22))

	#price labels
	plabel1 = tk.Label(cnv,text = str(order_table[indexvals[0]-1][2]), font = ("marck script", 22))
	plabel2 = tk.Label(cnv,text = str(order_table[indexvals[1]-1][2]), font = ("marck script", 22))
	plabel3 = tk.Label(cnv,text = str(order_table[indexvals[2]-1][2]), font = ("marck script", 22))
	plabel4 = tk.Label(cnv,text = str(order_table[indexvals[3]-1][2]), font = ("marck script", 22))
	plabel5 = tk.Label(cnv,text = str(order_table[indexvals[4]-1][2]), font = ("marck script", 22))
	plabel6 = tk.Label(cnv,text = str(order_table[indexvals[5]-1][2]), font = ("marck script", 22))
	slabel1.place(x = 9, y = 1*60 - 14)
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

#order clear system

def internal_del_but():
	tno = int(del_en1.get())

	contd = "tablenum = %s" % (tno)

	mysql_c.delete_row("orders", contd)

	update_table_lis()
	clear_screen()
	screen_update()

def delete_box():
	global del_en1
	delete = tk.Tk()
	delete.geometry("400x400")

	la1 = tk.Label(delete, text = "t.no", font = ("marck script", 25))

	del_en1 = tk.Entry(delete)

	del_but = tk.Button(delete, text = "CLEAR", height = 2, width = 10, command = internal_del_but)

	la1.place(x = 90, y = 170)
	del_en1.place(x = 190, y = 170+16)
	del_but.place(x = 155, y = 260+16)




#navigation system
def next_box():# give an upper limit to these poor numbers, make it so that it deletes previous labels
	global indexvals

	if indexvals[5] == len(order_table):#at this point the numbers start peepin outta their boxes
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



orders = tk.Tk()
orders.geometry("1080x540")




########WIDGET CREATION##########
cnv = tk.Canvas(orders, height= 400, width = 800)
next_button = tk.Button(orders, text = "NEXT", height = 2, width = 10, command = next_box) 
prev_button = tk.Button(orders, text = "PREV", height = 2, width = 10, command = prev_box)
delete_button = tk.Button(orders, text = "DELETE", height = 2, width = 13, command = delete_box)


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
	tnum = tk.Label(cnv, text = "t.no", font = ("marck script", 16))
	descript = tk.Label(cnv, text = "Descript", font = ("marck script", 16))
	price = tk.Label(cnv, text = "Price", font = ("marck script", 16))

	tnum.place(x = 6, y = 6)
	descript.place(x = 322, y = 6)
	price.place(x=641+50, y = 6)

#main
update_table_lis()
table_form_creation()
next_button.place(x = 600, y = 55)
prev_button.place(x = 540-140, y = 55)
delete_button.place(x = 20, y = 139+70)
cnv.place(x = 139, y = 139)

orders.mainloop()

