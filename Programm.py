# __Author__ __Lencof__
# Programm.py

from tkinter import * 
from tkinter import filedialog 

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

mButton = Button(myApp,text = 'OK', command = mHello).pack()

#set the ment variable from the text entry box
nEntry = Entry(myApp,textvariable=ment).pack()

# create the menubar
menubar = Menu(myApp)

# create the file component of the menubar
filemenu = Menu(menubar, tearoff=0)

# Add the sub headings to the file menu
filemenu.add_command(Label="New", command=myNew)
filemenu.add_command(Label="Open", command=myOpen)
filemenu.add_command(Label="Save As...")
filemenu.add_command(Label="Close", command=mQuit)

menubar.add_cascade(Label="File",menu=filemenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(Label+"Help docs")
helpmenu.add_command(Label="About",command=mAbout)
menubar.add_cascade(Label="Help",menu=helpmenu)


# add menubarr to the window
myApp.config(menu=menubar)

myApp.mainloop() # close
