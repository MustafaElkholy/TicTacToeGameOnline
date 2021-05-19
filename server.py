from socket import*
from threading import Thread
from tkinter import*
from tkinter import messagebox
from _thread import*
import threading

s= socket(AF_INET,SOCK_STREAM)
host ="127.0.0.1"
port = 7000
s.bind((host,port))
s.listen(5)

c,ad=s.accept()

def recieve(c):
    while True:
        x = c.recv(200).decode('utf-8')
        if(x== 'a'and button1['text']==" "):
            button1["text"]='O'
        if(x== 'b'and button2['text']==" "):
            button2["text"]='O'
        if(x== 'c'and button3['text']==" "):
            button3["text"]='O'
        if(x== 'd'and button4['text']==" "):
            button4["text"]='O'
        if(x== 'e'and button5['text']==" "):
            button5["text"]='O'
        if(x== 'f'and button6['text']==" "):
            button6["text"]='O'
        if(x == 'g'and button7['text']==" "):
            button7["text"]='O'
        if(x == 'h'and button8['text']==" "):
            button8["text"]='O'
        if(x == 'i'and button9['text']==" "):
            button9["text"]='O'
        check()
        
start_new_thread(recieve,(c,))


def send(x):
    c.send(x.encode('utf-8'))
    
window = Tk()

window.title("Tik tak toe ")
window.geometry("400x300")

label1 = Label(window, text="player 1: X",font=('Helvectica','14'))
label1.grid(row=0,column=0)


def Button1():
    if (button1["text"]==" "):
        button1["text"]='X'
        send('a')
    check()

def Button2():
    if (button2["text"]==" "):
        button2["text"]='X'
        send('b')
    check()
        
def Button3():
    if (button3["text"]==" "):
        button3["text"]='X'
        send('c')
    check()
        
def Button4():
    if (button4["text"]==" "):
        button4["text"]='X'
        send('d')
        check()
        
def Button5():
    if (button5["text"]==" "):
        button5["text"]='X'
        send('e')
    check()
        
def Button6():
    if (button6["text"]==" "):
        button6["text"]='X'
        send('f')
    check()
        
def Button7():
    if (button7["text"]==" "):
        button7["text"]='X'
        send('g')
    check()
        
def Button8():
    if (button8["text"]==" "):
        button8["text"]='X'
        send('h')
    check()
        
def Button9():
    if (button9["text"]==" "):
        button9["text"]='X'
        send('i')
    check()
        
        

    
button1 = Button(window, text=" ",bg="grey", fg="black",width=3,height=3,font=("Helvtica","14"),command=Button1)
button1.grid(row=0,column=1)

button2 = Button(window, text=" ",bg="grey", fg="black",width=3,height=3,font=("Helvtica","14"),command=Button2)
button2.grid(row=0,column=2)

button3 = Button(window, text=" ",bg="grey", fg="black",width=3,height=3,font=("Helvtica","14"),command=Button3)
button3.grid(row=0,column=3)

button4 = Button(window, text=" ",bg="grey", fg="black",width=3,height=3,font=("Helvtica","14"),command=Button4)
button4.grid(row=1,column=1)

button5 = Button(window, text=" ",bg="grey", fg="black",width=3,height=3,font=("Helvtica","14"),command=Button5)
button5.grid(row=1,column=2)

button6 = Button(window, text=" ",bg="grey", fg="black",width=3,height=3,font=("Helvtica","14"),command=Button6)
button6.grid(row=1,column=3)

button7 = Button(window, text=" ",bg="grey", fg="black",width=3,height=3,font=("Helvtica","14"),command=Button7)
button7.grid(row=2,column=1)

button8 = Button(window, text=" ",bg="grey", fg="black",width=3,height=3,font=("Helvtica","14"),command=Button8)
button8.grid(row=2,column=2)

button9 = Button(window, text=" ",bg="grey", fg="black",width=3,height=3,font=("Helvtica","14"),command=Button9)
button9.grid(row=2,column=3)


TotalTurns = 0
def check():
    global TotalTurns
    TotalTurns = TotalTurns+1
    
    b1=button1["text"]
    b2=button2["text"]
    b3=button3["text"]
    b4=button4["text"]
    b5=button5["text"]
    b6=button6["text"]
    b7=button7["text"]
    b8=button8["text"]
    b9=button9["text"]
    
    if(b1==b2  and b2==b3 and b1=='O' or b1==b2 and b2==b3 and b1=='X'):
        win(b1)
    if(b4==b5  and b5==b6 and b4=='O' or b4==b5 and b5==b6 and b4=='X'):
        win(b4)
    if(b7==b8  and b8==b9  and b7=='O' or b7==b8 and b8==b9 and b7=='X'):
        win(b7)
    if(b1==b4  and b4==b7  and b1=='O' or b1==b4 and b4==b7 and b1=='X'):
        win(b1)
    if(b2==b5  and b5==b8  and b2=='O' or b2==b5 and b5==b8 and b2=='X'):
        win(b2)
    if(b3==b6  and b6==b9  and b3=='O' or b3==b6 and b6==b9 and b3=='X'):
        win(b3)
    if(b1==b5  and b5==b9  and b1=='O' or b1==b5 and b5==b9 and b1=='X'):
        win(b1)
    if(b3==b5  and b5==b7  and b3=='O' or b3==b5 and b5==b7 and b3=='X'):
        win(b3)
    
    if TotalTurns==10:
        messagebox.showinfo('Draw')
        window.destroy()
        
def win(player):
    messagebox.showinfo("The winner is ", player)
    window.destroy()
   

window.mainloop() 
