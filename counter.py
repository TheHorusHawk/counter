from Tkinter import *
import datetime
import os.path

name_of_file = "contador.csv"
if not os.path.isfile(name_of_file):
	f = open(nome_do_ficheiro, "w")
	f.write("Entradas no espaco\nDia do mes, mes, dia da semana, hora\n")

f = open(name_of_file, "a")

def append_line():
	line = datetime.datetime.strftime(datetime.datetime.now(), "%d,%b,%A,%H:%M") + "," + guest_value.get() + "\n"
	print guest_value.get
	f.write(line)

root = Tk()

guest_value = StringVar()
count_button = Button(root, text="Clica para gravar entrada", command=append_line)
guest = Checkbutton(root, text="Convidado?", variable = guest_value, onvalue="Convidado", offvalue = "Visitante").pack()
count_button.pack()

root.mainloop()
