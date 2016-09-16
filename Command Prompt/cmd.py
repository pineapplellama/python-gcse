# A basic Command Processor in Python 3.4
# Coded by Bohdan Pike; Version 1.1 - 27/02/2015

# Changelog:
#
# 1.0 - Started with base code. Works in most places except current path updates and changing current directory.
# 1.1 - Fixed current path updates and changing current directories. No known bugs currently.
# 1.2 - Added the custom command: "Version" and added automatic Microsoft Windows version updater. str(os.system("ver")) This checks Window's version and displays it.

import os
global root
global X
global Version
Version = "1.1"


root = os.getcwd() # Root is the current path of the command processor. This sets the starting default as the program's current working directory. (CWD)
os.chdir(root) # This changes the current path to the current working directory.

str(os.system("ver")) # This checks the system's version and displays it.
print("(c) 2015 Bohdan Pike. All rights reserved.")
os.system("title Command Prompt") # Sets the title.

X = "Foo" # Foo is the default for X when it needs to be reset. This is to stop looping errors.

while True: # Creates an infinite loop
    if X == "":
        X = input(root + ">") 
    elif "cd" in X:
        try:
            place = X.split(" ")[1]
            X = X.split(" ")[1]
            os.chdir(place)
            root = place
            X = input("\n" + root + ">")
        except:
            X = "Foo"
    elif X.lower() == "version":
        print("Command Processor by Bohdan Pike.\nVersion " + Version)
        X = "Foo"
    else: # Else;
        X = input("\n" + root + ">")


    if X == "Foo":
        pass
    elif X.lower() == "version":
        pass
    else:
        os.system(X)
