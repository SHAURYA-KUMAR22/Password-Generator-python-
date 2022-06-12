import random

from tkinter import *
import pyperclip 
from tkinter.ttk import *#special buttons
from PIL  import Image,ImageTk

def generate():

    entry.delete(0,END)#clears the display before generating
    low = "abcdefghijklmnopqrstuvwxyz"
    medium = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    strong = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password=""      
    passlen=v.get()
    if v1.get()==0:
        for i in range(0,passlen):
            password=password+random.choice(low)
        return password 
    elif v1.get()==1:
        for i in range(0,passlen):
            password=password+random.choice(medium)
        return password
    elif v1.get()==2: 
        for i in range(0,passlen): 
            password = password + random.choice(strong) 
        return password 
        
def display(): 
    pass1=generate() 
    entry.insert(0,pass1)#inserts paas1 to password
def copy1(): 
    random_password = entry.get() 
    pyperclip.copy(random_password) 
  
root=Tk()
root.resizable(False,False)
v= IntVar()#associated with passlength 
v1= IntVar()#associated with options or buttons
root.geometry('400x100')
load=Image.open('C:\\Users\\SHAURYA\\Desktop\\password generator\\code.jpg')
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)
root.title("RANDOM PASSWORD GENERATOR")
r_password = Label(root, text="Password",foreground="White",background="green3")
r_password.grid(row=6,column=0) 
entry=Entry(root)
entry.grid(row=6,column=1)
label1=Label(root,text="Length",foreground="White",background="green3")
label1.grid(row=2,column=0)
entry1=Entry(root,textvariable=v)
entry1.grid(row=2,column=1)
generate_b = Button(root, text="Generate", command=display)
generate_b.grid(row=4,column=1)
copy_button = Button(root, text="Copy", command=copy1) 
copy_button.grid(row=8, column=1) 
b_low = Radiobutton(root, text="low", variable=v1, value=0)
b_low.grid(row=2, column=3)
b_medium = Radiobutton(root, text="medium", variable=v1, value=1)
b_medium.grid(row=2, column=4)
b_strong = Radiobutton(root, text="strong", variable=v1, value=2)
b_strong.grid(row=2, column=5)
root.mainloop()
