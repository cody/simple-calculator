#simple calculator

from audioop import mul
from sqlite3 import OperationalError
import tkinter
from tkinter import DISABLED, Entry, font
from tkinter.ttk import LabelFrame
from tkinter import RIGHT, END, DISABLED, NORMAL
from unicodedata import decimal

#define window
root = tkinter.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(0,0)


#define colors and fonts
darkgreen = "black"
lightgreen = "black"
whitegreen = "black"

buttonfont = ("Arial", 18)
displayfont = ("Arial", 30)


#define functions
def submitnumber(number):
    '''add decimal or numebr to deisplay'''
    #insert number or dec pressed to end of display
    display.insert(END, number)

    #if decimal button was pressed, disable it so irt cant be pressed twice
    if "." in display.get():
        decimalbutton.config(state=DISABLED)


def operate(operator):
    '''store first number of expression and the operation to be used'''
    global firstnumber
    global operation

    #get the operator pressed and the current value of the display. this is the first numbe rin the clauclation
    operation = operator
    firstnumber = display.get()

    #delete the value (firstnumber) from the entry display
    display.delete(0, END)

    #disable all operator buttons until equal or clear is pressed
    addbutton.config(state=DISABLED)
    subtractbutton.config(state=DISABLED)
    multiplybutton.config(state=DISABLED)
    dividebutton.config(state=DISABLED)
    exponentbutton.config(state=DISABLED)
    inversebutton.config(state=DISABLED)
    squarebutton.config(state=DISABLED)

    #return dec button to normal state
    decimalbutton.config(state=NORMAL)

def equal():
    #run stored op for two numbers
    #perform the desired math
    if operation == "add":
        value = float(firstnumber) + float(display.get())
    elif operation == "subtract":
        value = float(firstnumber) - float(display.get())
    elif operation == "multiply":
        value = float(firstnumber) * float(display.get())
    elif operation == "divide":
        if display.get() == "0":
            value = "ERROR"
        else:
            value = float(firstnumber) / float(display.get())
    elif operation == "exponent":
        value = float(firstnumber) ** float(display.get())
    
    #remove the current value of the dispaly and update wirth current answer
    display.delete(0, END)
    display.insert(0, value)

    #return the buttons to the normal state
    enablebuttons()


def enablebuttons():
    #enable all buttons on calculator
    decimalbutton.config(state=NORMAL)
    addbutton.config(state=NORMAL)
    subtractbutton.config(state=NORMAL)
    multiplybutton.config(state=NORMAL)
    dividebutton.config(state=NORMAL)
    exponentbutton.config(state=NORMAL)
    inversebutton.config(state=NORMAL)
    squarebutton.config(state=NORMAL)


def clear():
    '''clear the display'''
    display.delete(0, END)

    #return buttons to normal state after pressing clear
    enablebuttons()

def inverse():
    #calc the inverse of a given number
    #do not allow for 1/0
    if display.get() == "0":
        value = "ERROR"
    else:
        value = 1/float(display.get())
    
    #remove the current value in the display and update it with the answer
    display.delete(0, END)
    display.insert(0, value)

def square():
    '''calc the quare of a given number'''
    value = float(display.get())**2

    #remove the current value in the display and update it with the answer
    display.delete(0, END)
    display.insert(0, value)

def negate():
    '''negate a given number'''
    value = -1*float(display.get())

    #remove the current value in the display and update it with the answer
    display.delete(0, END)
    display.insert(0, value)



#GUI layout
#define frames
displayframe = tkinter.LabelFrame(root) #create the display
displayframe.pack(padx=2, pady=(5,20)) #pack display on screen
buttonframe = tkinter.LabelFrame(root) #create frame that holds all the buttons
buttonframe.pack(padx=2, pady=5) #pack the button frame on the screen

#layout for the display frame
display = tkinter.Entry(displayframe, width=50, font=displayfont, bg=whitegreen, borderwidth=5, justify=RIGHT)
display.pack(padx=5, pady=5)


#layout for button frame
clearbutton = tkinter.Button(buttonframe, text="Clear", font=buttonfont, bg=darkgreen, command=clear)
quitbutton = tkinter.Button(buttonframe, text="Quit", font=buttonfont, bg=darkgreen, command=root.destroy)

inversebutton = tkinter.Button(buttonframe, text="1/x", font=buttonfont, bg=lightgreen, command=inverse)
squarebutton = tkinter.Button(buttonframe, text="x^2", font=buttonfont, bg=lightgreen, command=square)
exponentbutton = tkinter.Button(buttonframe, text="x^n", font=buttonfont, bg=lightgreen, command=lambda:operate("exponent"))
dividebutton = tkinter.Button(buttonframe, text=" / ", font=buttonfont, bg=lightgreen, command=lambda:operate("divide"))
multiplybutton = tkinter.Button(buttonframe, text="*", font=buttonfont, bg=lightgreen, command=lambda:operate("multiply"))
subtractbutton = tkinter.Button(buttonframe, text="-", font=buttonfont, bg=lightgreen, command=lambda:operate("subtract"))
addbutton = tkinter.Button(buttonframe, text="+", font=buttonfont, bg=lightgreen, command=lambda:operate("add"))
equalbutton = tkinter.Button(buttonframe, text="=", font=buttonfont, bg=darkgreen, command=equal)
decimalbutton = tkinter.Button(buttonframe, text=".", font=buttonfont, command=lambda:submitnumber("."))
negatebutton = tkinter.Button(buttonframe, text="+/-", font=buttonfont, command=negate)

ninebutton = tkinter.Button(buttonframe, text="9", font=buttonfont, command=lambda:submitnumber(9))
eightbutton = tkinter.Button(buttonframe, text="8", font=buttonfont, command=lambda:submitnumber(8))
sevenbutton = tkinter.Button(buttonframe, text="7", font=buttonfont, command=lambda:submitnumber(7))
sixbutton = tkinter.Button(buttonframe, text="6", font=buttonfont, command=lambda:submitnumber(6))
fivebutton = tkinter.Button(buttonframe, text="5", font=buttonfont, command=lambda:submitnumber(5))
fourbutton = tkinter.Button(buttonframe, text="4", font=buttonfont, command=lambda:submitnumber(4))
threebutton = tkinter.Button(buttonframe, text="3", font=buttonfont, command=lambda:submitnumber(3))
twobutton = tkinter.Button(buttonframe, text="2", font=buttonfont, command=lambda:submitnumber(2))
onebutton = tkinter.Button(buttonframe, text="1", font=buttonfont, command=lambda:submitnumber(1))
zerobutton = tkinter.Button(buttonframe, text="0", font=buttonfont, command=lambda:submitnumber(0))

#first row
clearbutton.grid(row=0, column=0, columnspan=2, pady=1, sticky="WE")
quitbutton.grid(row=0, column=2, columnspan=2, pady=1, sticky="WE")


#second row
inversebutton.grid(row=1, column=0, pady=1, sticky="WE")
squarebutton.grid(row=1, column=1, pady=1, sticky="WE")
exponentbutton.grid(row=1, column=2, pady=1, sticky="WE")
dividebutton.grid(row=1, column=3, pady=1, sticky="WE")

#third row (add padding to create the size of the column)
sevenbutton.grid(row=2, column=0, sticky="WE", pady=1, ipadx=10)
eightbutton.grid(row=2, column=1, sticky="WE", pady=1, ipadx=10)
ninebutton.grid(row=2, column=2, sticky="WE", pady=1, ipadx=10)
multiplybutton.grid(row=2, column=3, sticky="WE", pady=1, ipadx=10)

#fourth row
fourbutton.grid(row=3, column=0, pady=1, sticky="WE")
fivebutton.grid(row=3, column=1, pady=1, sticky="WE")
sixbutton.grid(row=3, column=2, pady=1, sticky="WE")
subtractbutton.grid(row=3, column=3, pady=1, sticky="WE")

#fifth row
onebutton.grid(row=4, column=0, pady=1, sticky="WE")
twobutton.grid(row=4, column=1, pady=1, sticky="WE")
threebutton.grid(row=4, column=2, pady=1, sticky="WE")
addbutton.grid(row=4, column=3, pady=1, sticky="WE")

#sixth row
negatebutton.grid(row=5, column=0, pady=1, sticky="WE")
zerobutton.grid(row=5, column=1, pady=1, sticky="WE")
decimalbutton.grid(row=5, column=2, pady=1, sticky="WE")
equalbutton.grid(row=5, column=3, pady=1, sticky="WE")

#run root window's main loop

root.mainloop()