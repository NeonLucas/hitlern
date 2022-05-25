import tkinter as tk
import mysql_c

def update_del_snos(sno):
	mysql_c.update_table("menu", "sno = sno - 1", "sno > %s" % (sno) )


def delete_button():#HAVE NOT DONE AUTO SNO UPDATE YET
	sno = int(en1.get())

	contd = "sno = %s" % (sno)

	mysql_c.delete_row("menu", contd)
	update_del_snos(sno)


def delete_box():
	global en1
	delete = tk.Tk()
	delete.geometry("400x400")

	la1 = tk.Label(delete, text = "Sno", font = ("marck script", 25))

	en1 = tk.Entry(delete)

	del_but = tk.Button(delete, text = "DELETE", height = 2, width = 10, command = delete_button)

	la1.place(x = 90, y = 170)
	en1.place(x = 190, y = 170+16)
	del_but.place(x = 155, y = 260+16)
