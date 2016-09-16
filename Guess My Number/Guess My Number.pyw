import time
from tkinter import *
from random import random
from tkinter import messagebox

Guesses=10

window = Tk() # This assigns "window" to a Tkinter GUI
try:
        window.iconbitmap('Question.ico') # This adds my icon
except:
        print("Can't find icon file; Question.ico. Ignoring.")
window.title("Guess My Number") # This sets the title
window["padx"] = 70 # This adds some padding of the window on the X cord
window["pady"] = 20 # This adds some padding of the window on the y cord

def About(): 
	messagebox.showinfo("About", "'Guess My Number' is made and coded by Bohdan Pike.\nVersion 2.\nThanks for Playing!")

def Contact():
	messagebox.showinfo("Contact", "You can contact me at: 'admin@bohdan.co'")

def Close():
	exit()

global DEBUG # This makes a DEBUG boolean
DEBUG = False

global guessnum
guessnum = "0"


def Guess(): # This defines what the button does
	if DEBUG == True:
		print("DEBUG: Button Pressed")
		print("DEBUG: guessnum = {}".format(guessnum))
		print("DEBUG: entryWidget = {}".format(entryWidget.get))
	guessnum=entryWidget.get() # This gets the stuff from the entry box
	if guessnum.isdigit():
		if Guesses == 0:
			messagebox.showerror("Out of Guesses", "Sorry, Out of guesses. Program will close in 2 seconds.")
			time.sleep(2)
			exit()
		if int(guessnum) == int(Number):
			messagebox.showinfo("Correct!", "Well Done!")
			time.sleep(2)
			exit()
		elif int(guessnum) >= int(Number):
			messagebox.showwarning("Too Big!", "Your guess was too big.")
			global Guesses
			Guesses -= 1
		elif int(guessnum) <= int(Number):
			messagebox.showwarning("Too Small!", "Your guess was too small.")
			global Guesses
			Guesses -=  1
		label1 = Label(window, text="You have {} guesses left.".format(Guesses)) # Adds a label that shows how many guesses you have left.
		label1.grid(row=0,column=0)
		window.update()
	else:
		messagebox.showerror("Error", "Please enter a whole number between 0-100")
		
        
Number = (round(random() * 100)) # This generates a random number between 0-100

if DEBUG == True:
	print("DEBUG MODE ACTIVE")
	print("DEBUG: The number is: {}".format(Number))

menubar=Menu(window)
filemenu = Menu(menubar)
filemenu.add_command(label="Exit",command = Close)
menubar.add_cascade(label="File",menu=filemenu) # This compiles all commands under filemenu into a list titled file and assigns the list to menubar

helpmenu = Menu(window)
helpmenu.add_command(label="About",command = About)
helpmenu.add_command(label="Contact",command = Contact)
menubar.add_cascade(label="Help",menu=helpmenu) # This compiles all commands under helpmenu into a list titled help and assigns the list to menubar

window.config(menu=menubar)

entryWidget=Entry(window,textvariable=guessnum) # This makes my entry box
entryWidget.grid(row=1,column=0) # And puts it in a grid

button = Button(window, text="Guess", command=Guess) # This makes my button
button.grid(row=2,column=0) # And adds it to the grid


window.mainloop() # Remove this for Unix based systems as it causes them to crash
