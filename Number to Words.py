from cProfile import label
from gc import disable
from tkinter import *
from num2words import num2words

#Gui and parameters init
root = Tk()
root.title("Number to Words")
root.geometry("800x400")

test = Label(root, text = "Enter the number below that you want to convert into words").grid(row=0 ,column=0)
e = Entry(root, width=15, borderwidth=5)
e.grid(row=1,column=0)

def myClick():
    convertedNumber = num2words(e.get())
    myLabel = Label(root, text = convertedNumber)
    myLabel.grid(row=3,column=0)

calculateButton = Button(root,text="Calculate: ", command=myClick)
calculateButton.grid(row=2,column=0)


root.mainloop()