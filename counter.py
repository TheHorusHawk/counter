from Tkinter import *
import datetime
import os.path

#initializes variable that defines name of csv file to save the timestamp to
name_of_file = "contador.csv"

#Creates csv file should it not exist
if not os.path.isfile(name_of_file):
	f = open(name_of_file, "w")
	f.write("Entradas no espaco\nDia do mes, mes, dia da semana, hora, convidado\n")

#opens file
f = open(name_of_file, "a")

#creates a count value that updates everytime line is added to csv file
count = 0
#function that writes to the csv file a new line with the timestamp and updates count
def append_line(*args):
	global count, label_text
	line = datetime.datetime.strftime(datetime.datetime.now(), "%d,%b,%A,%H:%M") + "," + guest_value.get() + "\n"
	count = count + 1	
	label_text.set(str(count) + " visitantes inseridos")
	f.write(line)

root = Tk()
frame = Frame(root)
frame.pack()

#initializes both StringVar variables, one for the last column and one for the label
guest_value = StringVar()
label_text = StringVar()

#generates button to press to add a line to file and checkbox that defines last column value
count_button = Button(frame, text="Clica para gravar entrada, ou clica Space", command=append_line)
guest = Checkbutton(frame, text="Convidado?", variable = guest_value, onvalue="Sim", offvalue = "").pack()
count_button.pack()

#binds spacekey to append_line function
root.bind("<space>",append_line)

#generates label that keeps track of how many lines were inserted
contador = Label(frame, textvariable=label_text)
contador.pack()	

root.mainloop()
