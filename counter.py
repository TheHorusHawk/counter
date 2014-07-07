from Tkinter import *
import datetime
import os.path

nome_do_ficheiro = "contador.csv"
if not os.path.isfile(nome_do_ficheiro):
	f = open(nome_do_ficheiro, "w")
	f.write("Entradas no espaco\nDia do mes, mes, dia da semana, hora\n")

f = open(nome_do_ficheiro, "a")
print f

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.count_button = Button(frame, text="Clica para gravar entrada", command=self.append_line)
        self.count_button.pack()

    def append_line(self):
	line = datetime.datetime.strftime(datetime.datetime.now(), "%d,%b,%A,%H:%M") + "\n"
        f.write(line)

root = Tk()

app = App(root)

root.mainloop()
# root.destroy()
