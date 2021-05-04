import tkinter
from tkinter import messagebox
import os
import array
import numpy
root=tkinter.Tk()
root.geometry("240x250")
root.title('Tic Tac Toe')

play1=[0,0,0,0,0,0,0,0,0]

xx=1
TT=7

    
    
def clear():
    def fun(number):
        global xx
        global TT
        play1.pop(number)#game changer
        
        if(number==0):
            if(xx%2==0):
                k1.config(text="X")
                play1.insert(0,"X")
                k1["state"]=tkinter.DISABLED
            elif(xx%2!=0):
                k1.config(text="O")
                play1.insert(0,"O")
                k1["state"]=tkinter.DISABLED

        if(number==1):
            if(xx%2==0):
                k2.config(text="X")
                play1.insert(1,"X")
                k2["state"]=tkinter.DISABLED
            elif(xx%2!=0):
                k2.config(text="O")
                play1.insert(1,"O")
                k2["state"]=tkinter.DISABLED

        if(number==2):
            if(xx%2==0):
                k3.config(text="X")
                play1.insert(2,"X")
                k3["state"]=tkinter.DISABLED
            elif(xx%2!=0):
                k3.config(text="O")
                play1.insert(2,"O")
                k3["state"]=tkinter.DISABLED

        if(number==3):
            if(xx%2==0):
                k4.config(text="X")
                play1.insert(3,"X")
                k4["state"]=tkinter.DISABLED
            elif(xx%2!=0):
                k4.config(text="O")
                play1.insert(3,"O")
                k4["state"]=tkinter.DISABLED

        if(number==4):
            if(xx%2==0):
                k5.config(text="X")
                play1.insert(4,"X")
                k5["state"]=tkinter.DISABLED
            elif(xx%2!=0):
                k5.config(text="O")
                play1.insert(4,"O")
                k5["state"]=tkinter.DISABLED

        if(number==5):
            if(xx%2==0):
                k6.config(text="X")
                play1.insert(5,"X")
                k6["state"]=tkinter.DISABLED
            elif(xx%2!=0):
                k6.config(text="O")
                play1.insert(5,"O")
                k6["state"]=tkinter.DISABLED

        if(number==6):
            if(xx%2==0):
                k7.config(text="X")
                play1.insert(6,"X")
                k7["state"]=tkinter.DISABLED
            elif(xx%2!=0):
                k7.config(text="O")
                play1.insert(6,"O")
                k7["state"]=tkinter.DISABLED

        if(number==7):
            if(xx%2==0):
                k8.config(text="X")
                play1.insert(7,"X")
                k8["state"]=tkinter.DISABLED
            elif(xx%2!=0):
                k8.config(text="O")
                play1.insert(7,"O")
                k8["state"]=tkinter.DISABLED

        if(number==8):
            if(xx%2==0):
                k9.config(text="X")
                play1.insert(8,"X")
                k9["state"]=tkinter.DISABLED
            elif(xx%2!=0):
                k9.config(text="O")
                play1.insert(8,"O")
                k9["state"]=tkinter.DISABLED
                
        xx=xx+1
        



    head.destroy()
    x.destroy()
    y.destroy()
    z.destroy()
    m=tkinter.Button(root,text="Player1 : X",width=10).grid(row=0,column=3)
    n=tkinter.Button(root,text="Player2 : O",width=10).grid(row=1,column=3)
    
    k1=tkinter.Button(root,width=9,bd=5,command=lambda:fun(0))
    k1.grid(row=2,column=0,ipady=17)
    k2=tkinter.Button(root,width=9,bd=5,command=lambda:fun(1))
    k2.grid(row=2,column=3,ipady=17)
    k3=tkinter.Button(root,width=9,bd=5,command=lambda:fun(2))
    k3.grid(row=2,column=4,ipady=17)
    k4=tkinter.Button(root,width=9,bd=5,command=lambda:fun(3))
    k4.grid(row=3,column=0,ipady=17)
    k5=tkinter.Button(root,width=9,bd=5,command=lambda:fun(4))
    k5.grid(row=3,column=3,ipady=17)
    k6=tkinter.Button(root,width=9,bd=5,command=lambda:fun(5))
    k6.grid(row=3,column=4,ipady=17)
    k7=tkinter.Button(root,width=9,bd=5,command=lambda:fun(6))
    k7.grid(row=4,column=0,ipady=17)
    k8=tkinter.Button(root,width=9,bd=5,command=lambda:fun(7))
    k8.grid(row=4,column=3,ipady=17)
    k9=tkinter.Button(root,width=9,bd=5,command=lambda:fun(8))
    k9.grid(row=4,column=4,ipady=17)
    
    





head = tkinter.Button(root, text = "---Welcome to tic-tac-toe---",activeforeground = 'red',
                      activebackground = "yellow", bg = "red",
                      fg = "yellow", width = 500, font = 'summer', bd = 5)



x = tkinter.Button(root, text = "Single Player",activeforeground = 'red',
                   activebackground = "yellow", bg = "red",fg = "yellow",
                   width = 500,font = 'summer', bd = 5)

y = tkinter.Button(root, text = "Multi Player", activeforeground = 'red',
                   activebackground = "yellow", bg = "red", fg = "yellow",
                   width = 500, font = 'summer', bd = 5,command=clear)

z = tkinter.Button(root, text = "Exit",activeforeground = 'red',
        activebackground = "yellow", bg = "red",fg = "yellow",width = 500,font = 'summer', bd = 5,command=root.destroy)


head.pack()
x.pack()
y.pack()
z.pack()

root.mainloop()

l=array.array('u',play1)
jjj=0
xxx=0
if((l[0]==l[1]==l[2]=='X')or
   (l[3]==l[4]==l[5]=='X')or
   (l[6]==l[7]==l[8]=='X')or
   (l[0]==l[3]==l[6]=='X')or
   (l[1]==l[4]==l[7]=='X')or
   (l[2]==l[5]==l[8]=='X')or
   (l[0]==l[4]==l[8]=='X')or
   (l[2]==l[4]==l[6]=='X')):
    messagebox.showinfo("Who Win","Player1 win")
    xxx=2

    
if((l[0]==l[1]==l[2]=='O')or
   (l[3]==l[4]==l[5]=='O')or
   (l[6]==l[7]==l[8]=='O')or
   (l[0]==l[3]==l[6]=='O')or
   (l[1]==l[4]==l[7]=='O')or
   (l[2]==l[5]==l[8]=='O')or
   (l[0]==l[4]==l[8]=='O')or
   (l[2]==l[4]==l[6]=='O')):
    messagebox.showinfo("Who Win","Player2 win")
    jjj=2


if(jjj==2 and xxx==2):
    messagebox.showinfo("Who Win","Hence Match tied")
    
elif(jjj!=2 and xxx!=2):
    messagebox.showinfo("Who Win","No one win")




    
