import tkinter as tk
import mysql_c

#debug line
#mysql_c.init_connection(host = "localhost", user = "root", passwd = "sachu123", database = "hitlern")

def sno_create():
	snolist = mysql_c.select_dat(table = "menu", columns = "sno")
	if snolist == []:
		max_sno = 0
	else:
		max_sno = max(max(snolist))

	return max_sno + 1

def enter_button():#need to automate the sno section completely
	sno = sno_create()
	food = str(en2.get())
	price = int(en3.get())

	columns = "(%s, \"%s\", %s)" % (sno, food, price)

	mysql_c.insert_val("menu", "(sno, dish, price)", columns)


def add_box():
	global en2, en3
	add = tk.Tk()
	add.geometry("400x400")

#la1 and en1 were removed

	la2 = tk.Label(add, text = "Food", font = ("marck script", 25))
	la3 = tk.Label(add, text = "Price", font = ("marck script", 25))
 
	en2 = tk.Entry(add)
	en3 = tk.Entry(add)

	ent_but = tk.Button(add, text = "ENTER", height = 2, width = 10, command = enter_button)

	la2.place(x = 90, y = 160)
	la3.place(x = 90, y = 210)
	
	en2.place(x = 190, y = 160+16)
	en3.place(x = 190, y = 210+16)

	ent_but.place(x = 155, y = 260+16)
	add.mainloop()