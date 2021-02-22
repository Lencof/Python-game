# __Author__ __Lencof__
# Programm.py

import sys # use sys
from tkinter import * 
from tkinter import filedialog # use filedialog

def mHello():
    mText=ment.get()
    mlabel1 = Label = Label(myApp,text=mText).pack()
    
def myNew():
    mlabel1 = Label(myApp,text="YO").pack()
    
def myOpen():
    myOpen = filedialog.askopenfile()
    mlabe14 = Label(myApp,text=myOpen).pack()
    
def mAbout():
    messagebox.showinfo(title="About",message="This is the about box")

def mQuit():
    mExit = messagebox.askyesno(title="Quit", message="Are you sure")
    if mExit > 0:
        myApp.destroy()    
        
        
myApp = tk()
# create a string variable
ment = StringVar()

# set the size of window
myApp.geometry('450x450+200+200')

myApp.title('MyApp')

mLabel = Label(myApp,text='my label').pack()

# I will add the code
