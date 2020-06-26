import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import time
import random

path_names = ['HM8.png','HM7.png','HM6.png','HM5.png','HM4.png','HM3.png']
chances=5
file=open("File.txt","r")
arr=[]
for line in file:
    nword=file.readline()
    nword=nword.upper()
    nword=nword.strip()
    arr.append(nword)
random.shuffle(arr)
word=arr[0]
master = tk.Tk()
master.title("Hangman")
master.config(bg="black")
master.resizable(0,0)
def click():
    tk.messagebox.showinfo("Rules","You will have to guess a random word.\nYou have 5 chances\nGet started!")
def clicked():
    tk.messagebox.showinfo("Alert!","You have already guessed it")

def check(str):
    if word.find(str) != -1:
        global output
        temp=""
        for position in range(len(word)):
            if str == word[position]:
               temp=temp+str
            else:
                temp=temp+output[position]
        output=temp
        display_txt.config(text=output)
        if(output == word):
            time.sleep(2)
            tk.messagebox.showinfo("Win","Congratulations!\nYou won.\nYou guessed the correct answer.\nIt was "+word+".")
            master.destroy()
    else:
        global chances
        global path_names
        chances=chances-1
        imgnew = Image.open(path_names[chances])
        imgnew = imgnew.resize((400, 300), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(imgnew)
        pic.config(image=imgnew)
        pic.image=imgnew

        if(chances<=0):
            time.sleep(2)
            tk.messagebox.showinfo("Lose", "Sorry.\nYou lost.\nThe correct answer was "+word+".\nBetter luck next time.")
            master.destroy()


def call_a():
    a.configure(bg="grey",fg="white",command=clicked)
    check("A")
def call_b():
    b.configure(bg="grey",fg="white",command=clicked)
    check("B")
def call_c():
    c.configure(bg="grey",fg="white",command=clicked)
    check("C")
def call_d():
    d.configure(bg="grey",fg="white",command=clicked)
    check("D")
def call_e():
    e.configure(bg="grey",fg="white",command=clicked)
    check("E")
def call_f():
    f.configure(bg="grey",fg="white",command=clicked)
    check("F")
def call_g():
    g.configure(bg="grey",fg="white",command=clicked)
    check("G")
def call_h():
    h.configure(bg="grey",fg="white",command=clicked)
    check("H")
def call_i():
    i.configure(bg="grey",fg="white",command=clicked)
    check("I")
def call_j():
    j.configure(bg="grey",fg="white",command=clicked)
    check("J")
def call_k():
    k.configure(bg="grey",fg="white",command=clicked)
    check("K")
def call_l():
    l.configure(bg="grey",fg="white",command=clicked)
    check("L")
def call_m():
    m.configure(bg="grey",fg="white",command=clicked)
    check("M")
def call_n():
    n.configure(bg="grey",fg="white",command=clicked)
    check("N")
def call_o():
    o.configure(bg="grey",fg="white",command=clicked)
    check("O")
def call_p():
    p.configure(bg="grey",fg="white",command=clicked)
    check("P")
def call_q():
    q.configure(bg="grey",fg="white",command=clicked)
    check("Q")
def call_r():
    r.configure(bg="grey",fg="white",command=clicked)
    check("R")
def call_s():
    s.configure(bg="grey",fg="white",command=clicked)
    check("S")
def call_t():
    t.configure(bg="grey",fg="white",command=clicked)
    check("T")
def call_u():
    u.configure(bg="grey",fg="white",command=clicked)
    check("U")
def call_v():
    v.configure(bg="grey",fg="white",command=clicked)
    check("V")
def call_w():
    w.configure(bg="grey",fg="white",command=clicked)
    check("W")
def call_x():
    x.configure(bg="grey",fg="white",command=clicked)
    check("X")
def call_y():
    y.configure(bg="grey",fg="white",command=clicked)
    check("Y")
def call_z():
    z.configure(bg="grey",fg="white",command=clicked)
    check("Z")

def modify(str):
    le=len(str)
    modific=""
    for pos in range(le):
        modific+="*"
    return modific

tk.Button(master,text="Rules",bg="Black",fg="grey",width=20,command=click).grid(row=0,column=0,columnspan=5,sticky="W")
tk.Label(master,text="No. of characters : "+str(len(word)),bg="black",fg="grey").grid(row=0,column=4,columnspan=5,sticky="w")
img=Image.open(path_names[chances])
img=img.resize((400,300),Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
pic=tk.Label(master, image = img)
pic.grid(row=1,column=0, columnspan=10)
output=modify(word)
display_txt=tk.Label(master,text=output,bg="black",fg="white",height=5,width=30,font="arial 20 bold")
display_txt.grid(row=2,column=0,columnspan=30)
q=tk.Button(master,text="Q",bg="black",fg="grey",width=7,command=call_q)
w=tk.Button(master,text="W",bg="black",fg="grey",width=7,command=call_w)
e=tk.Button(master,text="E",bg="black",fg="grey",width=7,command=call_e)
r=tk.Button(master,text="R",bg="black",fg="grey",width=7,command=call_r)
t=tk.Button(master,text="T",bg="black",fg="grey",width=7,command=call_t)
y=tk.Button(master,text="Y",bg="black",fg="grey",width=7,command=call_y)
u=tk.Button(master,text="U",bg="black",fg="grey",width=7,command=call_u)
i=tk.Button(master,text="I",bg="black",fg="grey",width=7,command=call_i)
o=tk.Button(master,text="O",bg="black",fg="grey",width=7,command=call_o)
p=tk.Button(master,text="P",bg="black",fg="grey",width=7,command=call_p)
a=tk.Button(master,text="A",bg="black",fg="grey",width=7,command=call_a)
s=tk.Button(master,text="S",bg="black",fg="grey",width=7,command=call_s)
d=tk.Button(master,text="D",bg="black",fg="grey",width=7,command=call_d)
f=tk.Button(master,text="F",bg="black",fg="grey",width=7,command=call_f)
g=tk.Button(master,text="G",bg="black",fg="grey",width=7,command=call_g)
h=tk.Button(master,text="H",bg="black",fg="grey",width=7,command=call_h)
j=tk.Button(master,text="J",bg="black",fg="grey",width=7,command=call_j)
k=tk.Button(master,text="K",bg="black",fg="grey",width=7,command=call_k)
l=tk.Button(master,text="L",bg="black",fg="grey",width=7,command=call_l)
z=tk.Button(master,text="Z",bg="black",fg="grey",width=7,command=call_z)
x=tk.Button(master,text="X",bg="black",fg="grey",width=7,command=call_x)
c=tk.Button(master,text="C",bg="black",fg="grey",width=7,command=call_c)
v=tk.Button(master,text="V",bg="black",fg="grey",width=7,command=call_v)
b=tk.Button(master,text="B",bg="black",fg="grey",width=7,command=call_b)
n=tk.Button(master,text="N",bg="black",fg="grey",width=7,command=call_n)
m=tk.Button(master,text="M",bg="black",fg="grey",width=7,command=call_m)

q.grid(row=3,column=0,sticky="W")
w.grid(row=3,column=1,sticky="W")
e.grid(row=3,column=2,sticky="W")
r.grid(row=3,column=3,sticky="W")
t.grid(row=3,column=4,sticky="W")
y.grid(row=3,column=5,sticky="W")
u.grid(row=3,column=6,sticky="W")
i.grid(row=3,column=7,sticky="W")
o.grid(row=3,column=8,sticky="W")
p.grid(row=3,column=9,sticky="W")
a.grid(row=4,column=1,sticky="W")
s.grid(row=4,column=2,sticky="W")
d.grid(row=4,column=3,sticky="W")
f.grid(row=4,column=4,sticky="W")
g.grid(row=4,column=5,sticky="W")
h.grid(row=4,column=6,sticky="W")
j.grid(row=4,column=7,sticky="W")
k.grid(row=4,column=8,sticky="W")
l.grid(row=4,column=9,sticky="W")
z.grid(row=5,column=2,sticky="W")
x.grid(row=5,column=3,sticky="W")
c.grid(row=5,column=4,sticky="W")
v.grid(row=5,column=5,sticky="W")
b.grid(row=5,column=6,sticky="W")
n.grid(row=5,column=7,sticky="W")
m.grid(row=5,column=8,sticky="W")

tk.Label(master,text="Developed by Sagnik Nayak and Saraswat Majumder",bg="black",fg="grey").grid(row=7,column=0,columnspan=9,sticky="w")
master.mainloop()