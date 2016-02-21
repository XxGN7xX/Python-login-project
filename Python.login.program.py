from tkinter import *
import tkinter.messagebox as tm
import time
import webbrowser
window = Tk()
window.wm_title("Python login program")



#This is the username entry
Label(window, text = "Username:", bg = "light blue") .grid(column = 0, row = 0, sticky = W)
Username = Entry(window, width = 25)
Username .grid(column = 2, row = 0, sticky = W)

#This is the password entry
Label(window, text = "Password:", bg = "light blue") .grid(column = 0, row = 1, sticky = W)
Password = Entry(window, width = 25)
Password .grid (column = 2, row = 1, sticky = W)
      
#This is the login code
def Login():
    text = Username.get()
    text1 = Password.get()
    if text == "Uname" and text1 == "Pass":
        tm.showinfo("Correct", "Logging in")
        webbrowser.open("https://github.com/", new=0, autoraise = True)
    elif text != "Uname" or text1 != "Pass":
        tm.showinfo ("Incorrect", "Try again")

#This is the submit button
Button (window, height = 2, width = 5, text = "Submit", bg = "light blue", command = Login) .grid(column = 2, row = 4, sticky = W)

print ("Thank you for viewing my simple project on github (: if you enjoyed this project then please favourite this - and if you found this too easy you are likely beyond this level and should be doing something more advanced.")
print (" - Regards, Developer")

window.mainloop()

