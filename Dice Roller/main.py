debugMode = False
windowTitle = "Dice"
menuBarEnable = True

def ToggleDebug(e):
    global debugMode
    if debugMode is True:
        debugMode = False
    else:
        debugMode = True

def Contact():
    messagebox.showinfo("Contact", "You can contact me at: 'admin@bohdan.co'")

def About():
    messagebox.showinfo("About", "This dice game is made and coded by Bohdan Pike.\nVersion 1.\nThanks for Playing!")
    

def InterruptLoop():
    exit()

def Roll(e):
    currentNumber = randint(1,6)
    if debugMode is True:
        print(str(e) + ";{}".format(currentNumber))
    else:
        print("You rolled a {}! :D".format(currentNumber))
    i = 1
    for number in ["One", "Two", "Three", "Four", "Five", "Six"]:
        exec('if currentNumber == {}:display.config(image = {})'.format(i,number))
        if i <= 6:
            i = i + 1
    display.update()


from tkinter import *
from tkinter import messagebox
from random import randint

window = Tk()
window.title(windowTitle)
try:
    window.iconbitmap(".\Resources\icon.ico")
except TclError:
    if debugMode is True:
        print("Can't find icon file at; Catching exception.")
        

for number in ["One", "Two", "Three", "Four", "Five", "Six"]:
    source = "os.path.dirname(full_path)" + number + ".png\""
    exec('{} = PhotoImage(file={})'.format(number, source))


display = Label(window, image=One)
display.pack()
window.bind("<Return>", Roll)
window.bind("d", ToggleDebug)
window.resizable(0,0)



if menuBarEnable is True:
    menubar=Menu(window)
    filemenu = Menu(menubar)
    filemenu.add_command(label="Exit", command = InterruptLoop)
    menubar.add_cascade(label="File",menu=filemenu)

    helpmenu = Menu(window)
    helpmenu.add_command(label="About",command = About)
    helpmenu.add_command(label="Contact",command = Contact)
    menubar.add_cascade(label="Help",menu=helpmenu)

    window.config(menu=menubar)

messagebox.showinfo("How to use", "Press ENTER to roll the dice.")

window.mainloop()
