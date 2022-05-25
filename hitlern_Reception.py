import tkinter as tk

main = tk.Tk()


def customer():
	main.destroy()
	import Hitlern # dont forget the CAPITAL H big boi


customer_btn = tk.Button(main, text= "test", command = customer)

customer_btn.pack()
main.mainloop()