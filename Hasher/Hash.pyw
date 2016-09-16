# Code created by Bohdan Pike; 19/02/2015
# Version 1
# Uses colour config from Bohdan Pike's Calculator.pyw


from tkinter import *
import hashlib

# Do not change the line below please as it is a default upon launch.
Type = "MD5"

# Config
iconDirectory = ".\Hash.ico" # If this directory is broken, Python will notice the error and keep running using a default image instead.
background = "#171814" # Use #XXXXXX codes or the name of the colour E.G: BLACK or #000000
textcolour = "WHITE" # Use #XXXXXX codes or the name of the colour E.G: BLACK or #000000
objectbackground = "#272822" # Use #XXXXXX codes or the name of the colour E.G: BLACK or #000000
objectstyle = 0
objectstylenum = 5 # Any whole number
buttonsizex = 10
buttonsizey = 3
windowsizex = 40
windowsizey = 10



if objectstyle == True:
    objectstyle = objectstylenum
elif objectstyle == False:
    pass
    

if objectstylenum >= 50:
    messagebox.showerror("Error", "The config is not set up correctly; Please see line 5 of the config. (Value too big to render)")
    print("Config Error; objectstyle is out of bounds. Accepted values are 0-50")
    exit()

# What to do if type button clicked.
def Switch():
	global Type
	if Type == "MD5":
		window.title("Hash - SHA512")
		Type = "SHA512"
		window.update()
	elif Type == "SHA512":
		window.title("Hash - SHA384")
		Type = "SHA384"
		window.update()
	elif Type == "SHA384":
		window.title("Hash - SHA256")
		Type = "SHA256"
		window.update()
	elif Type == "SHA256":
		window.title("Hash - SHA224")
		Type = "SHA224"
		window.update()
	elif Type == "SHA224":
		window.title("Hash - SHA1")
		Type = "SHA1"
		window.update()
	elif Type == "SHA1":
		window.title("Hash - MD5")
		Type = "MD5"
		window.update()

# What to do if Hash File button clicked
def Hashfile(Y):
	if Type == "MD5":
		hash_object = hashlib.md5(open(Y, 'rb').read()).hexdigest()
		print(hash_object)
		print("\n")
		box.delete(0, END)
		box.insert(0, hash_object)
	elif Type == "SHA512":
		hash_object = hashlib.sha512(open(Y, 'rb').read()).hexdigest()
		print(hash_object)
		print("\n")
		box.delete(0, END)
		box.insert(0, hash_object)
	elif Type == "SHA384":
		hash_object = hashlib.sha384(open(Y, 'rb').read()).hexdigest()
		print(hash_object)
		print("\n")
		box.delete(0, END)
		box.insert(0, hash_object)
	elif Type == "SHA256":
		hash_object = hashlib.sha256(open(Y, 'rb').read()).hexdigest()
		print(hash_object)
		print("\n")
		box.delete(0, END)
		box.insert(0, hash_object)
	elif Type == "SHA224":
		hash_object = hashlib.sha224(open(Y, 'rb').read()).hexdigest()
		print(hash_object)
		print("\n")
		box.delete(0, END)
		box.insert(0, hash_object)
	elif Type == "SHA1":
		hash_object = hashlib.sha1(open(Y, 'rb').read()).hexdigest()
		print(hash_object)
		print("\n")
		box.delete(0, END)
		box.insert(0, hash_object)
	else:
		print("Error")
		print("Hash Type: {} not recognised".format(Type))

# What to do if Hash Text button clicked
def Hash(X):
	if Type == "MD5":
		hash_object = hashlib.md5(X.encode())
		print(hash_object.hexdigest())
		print("\n")
		box.delete(0, END)
		box.insert(0, hash_object.hexdigest())
	elif Type == "SHA512":
		hash_object = hashlib.sha512(X.encode())
		print(hash_object.hexdigest())
		print("\n")
		box.delete(0, END)
		box.insert(0, hash_object.hexdigest())
	elif Type == "SHA384":
		hash_object = hashlib.sha384(X.encode())
		print(hash_object.hexdigest())
		print("\n")
		box.delete(0, END)
		box.insert(0, hash_object.hexdigest())
	elif Type == "SHA256":
		hash_object = hashlib.sha256(X.encode())
		print(hash_object.hexdigest())
		print("\n")
		box.delete(0, END)
		box.insert(0, hash_object.hexdigest())
	elif Type == "SHA224":
		hash_object = hashlib.sha224(X.encode())
		print(hash_object.hexdigest())
		print("\n")
		box.delete(0, END)
		box.insert(0, hash_object.hexdigest())
	elif Type == "SHA1":
		hash_object = hashlib.sha1(X.encode())
		print(hash_object.hexdigest())
		print("\n")
		box.delete(0, END)
		box.insert(0, hash_object.hexdigest())
	else:
		print("Error")
		print("Hash Type: {} not recognised".format(Type))

window = Tk()
window.title("Hash - MD5")
window.config(bg=background)
try:
	window.iconbitmap(iconDirectory)
except:
	print("Can't find icon file; Hash.ico. Ignoring...")
window["padx"] = windowsizex
window["pady"] = windowsizey

# This prevents a bug with some older unix based systems as they don't like unresizeable windows.
try:
	window.resizable(0,0)
except:
	print("Unresizeable failed.")

box = Entry(window, bg=objectbackground, fg=textcolour, bd = objectstyle)
box.grid(row=0,column=0,columnspan=10,sticky=N, pady= 8)

butt = Button(window,text="Hash Text", bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex, command= lambda: Hash(box.get()))
butt.grid(row=1,column=0, sticky=W)

butf = Button(window,text="Hash File", bg=objectbackground, fg=textcolour, bd = objectstyle, height = buttonsizey, width = buttonsizex, command= lambda: Hashfile(box.get()))
butf.grid(row=1,column=1, sticky=E)

butf = Button(window,text="Type", bg=objectbackground, fg=textcolour, bd = objectstyle, height = 1, width = (buttonsizex*2)+1, command= lambda: Switch())
butf.grid(row=2,column=0,columnspan=2)

window.mainloop()
