
from tkinter import *

sameh = Tk()
sameh.geometry("600x600")
sameh.title("My Calculator Project")
def insert(text): # insert at entry when user not enter '=' character
    if text != "=":
       En.insert("end",text) # put characters inside entry
    else :
        try:
         operation = eval(En.get())  # using eval function for evaluation an expression that in entry
         En.delete(0,"end") # delete all characters in entry
         En.insert(0,"{}".format(operation))  # push the result of expression in entry
        except:
            En.delete(0,"end")
            En.insert(0,"Error !!!") # for avoiding exceptions

def button(text,col,ro):
    Button(sameh,bg="cyan",bd=7,width=25,font=10,height=1,activebackground="black",activeforeground="yellow",disabledforeground="green",text=text,command=lambda: insert(text)).grid(column=col,row=ro,ipady=30,ipadx=1)  
En = Entry(sameh,width=70,bd=6,border=20,font="arail 15",background="black",foreground="cyan")
En.grid(column=0,row=0,columnspan=3,ipadx=45,ipady=45)

button("1",0,1)
button("2",1,1)
button("3",2,1)

button("4",0,2)
button("5",1,2)
button("6",2,2)

button("7",0,3)
button("8",1,3)
button("9",2,3)
button("0",0,4)

button(".",1,4)
button("%",2,4)
button("+",0,5)

button("-",1,5)
button("*",2,5)
button("/",2,6)
button("=",1,6)



sameh.mainloop()