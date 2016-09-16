import sys
from tkinter import *
import tkinter.messagebox as messagebox


def About():
    messagebox.showinfo("About", "This calculator program is made and coded by Bohdan Pike.\nVersion 2.\n\n28/10/2014")



# Config
background = "#171814" # Use #XXXXXX codes or the name of the colour E.G: BLACK or #000000
textcolour = "WHITE" # Use #XXXXXX codes or the name of the colour E.G: BLACK or #000000
objectbackground = "#272822" # Use #XXXXXX codes or the name of the colour E.G: BLACK or #000000
objectstyle = 0
objectstylenum = 5 # Any whole number
buttonsizex = 8
buttonsizey = 3
windowsizex = 10
windowsizey = 10
highlightcolour = "#272822"
menucolour = "#5b5b5b"
FirstName = "Bohdan"
LastName = "Pike"


# Default Config

#background = "#171814" # Use #XXXXXX codes or the name of the colour E.G: BLACK or #000000
#textcolour = "WHITE" # Use #XXXXXX codes or the name of the colour E.G: BLACK or #000000
#objectbackground = "#272822" # Use #XXXXXX codes or the name of the colour E.G: BLACK or #000000
#objectstyle = 0 # Set to 0 for unstyled and 1 for styled
#objectstylenum = 5 # Any whole number
#buttonsizex = 8
#buttonsizey = 3
#windowsizex = 10
#windowsizey = 10
#highlightcolour = "#272822"
#menucolour = "#5b5b5b"


if objectstyle == True:
    objectstyle = objectstylenum
elif objectstyle == False:
    pass
    

if objectstylenum >= 50:
    messagebox.showerror("Error", "The config is not set up correctly; Please see line 5 of the config. (Value too big to render)")
    print("Config Error; objectstyle is out of bounds. Accepted values are 0-50")
    exit()


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False


    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)      
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op): 
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)





sum1 = Calc()
window = Tk()
window.title("Calculator")
#window.iconbitmap('Calc.ico')
window.config(bg=background)
window["padx"] = windowsizex
window["pady"] = windowsizey
window.resizable(0,0)



# Objects
text_box = Entry(window, bg=objectbackground, fg=textcolour, bd = objectstyle)
text_box.grid(row=0,column=0,columnspan=4,sticky=N, pady= 8)
text_box.insert(0,"0")


button1 = Button(window,text=1, bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
button1["command"] = lambda: sum1.num_press(1)
button1.grid(row=2,column=0, sticky=W)

button2 = Button(window,text=2, bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
button2["command"] = lambda: sum1.num_press(2)
button2.grid(row=2,column=1, sticky=N)

button3 = Button(window,text=3, bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
button3["command"] = lambda: sum1.num_press(3)
button3.grid(row=2,column=2, sticky=E)

button4 = Button(window,text=4, bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
button4["command"] = lambda: sum1.num_press(4)
button4.grid(row=3,column=0, sticky=W)

button5 = Button(window,text=5, bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
button5["command"] = lambda: sum1.num_press(5)
button5.grid(row=3,column=1, sticky=N)

button6 = Button(window,text=6, bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
button6["command"] = lambda: sum1.num_press(6)
button6.grid(row=3,column=2, sticky=E)

button7 = Button(window,text=7, bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
button7["command"] = lambda: sum1.num_press(7)
button7.grid(row=4,column=0, sticky=W)

button8 = Button(window,text=8, bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
button8["command"] = lambda: sum1.num_press(8)
button8.grid(row=4,column=1, sticky=N)

button9 = Button(window,text=9, bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
button9["command"] = lambda: sum1.num_press(9)
button9.grid(row=4,column=2, sticky=E)

button0 = Button(window,text=0, bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
button0["command"] = lambda: sum1.num_press(0)
button0.grid(row=5,column=1, sticky=N)

buttonequal = Button(window,text="=", bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
buttonequal["command"] = sum1.calc_total
buttonequal.grid(row=5,column=2, sticky=E)

buttondot = Button(window,text=".", bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
buttondot["command"] = lambda: sum1.num_press(".")
buttondot.grid(row=5,column=0, sticky=W)

buttonclear = Button(window,text="C", bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
buttonclear["command"] = sum1.cancel
buttonclear.grid(row=6,column=1, sticky=W)

buttoncleareverything = Button(window,text="CE", bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
buttoncleareverything["command"] = sum1.all_cancel
buttoncleareverything.grid(row=6,column=2, sticky=W)

buttonabout = Button(window,text="About", bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex, command = About)
buttonabout.grid(row=6,column=3, sticky=W)

buttonname = Button(window,text="{}\n{}".format(FirstName,LastName), bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
buttonname.grid(row=6,column=0, sticky=W)

buttonadd = Button(window,text="+", bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
buttonadd["command"] = lambda: sum1.operation("add")
buttonadd.grid(row=2,column=3, sticky=E)

buttonminus = Button(window,text="-", bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
buttonminus["command"] = lambda: sum1.operation("minus")
buttonminus.grid(row=3,column=3, sticky=E)

buttonmulti = Button(window,text="x", bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
buttonmulti["command"] = lambda: sum1.operation("times")
buttonmulti.grid(row=4,column=3, sticky=E)

buttondiv = Button(window,text=chr(247), bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex)
buttondiv["command"] = lambda: sum1.operation("divide")
buttondiv.grid(row=5,column=3, sticky=E)

window.mainloop()
