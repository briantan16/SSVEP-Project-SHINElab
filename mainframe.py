import tkinter as tk

import tkinter
from turtle import color

master=tkinter.Tk()
master.title("SSVEP GUI")
master.geometry("1000x700")

txt = tk.Label(master, text="", bg="black", fg="white", font=("Times New Roman", 20))

overall_str = ""



c = tk.Canvas(master, width=700, height=700, bg="black")

c.pack(pady = 120, padx=10)

q1_bool, q2_bool, q3_bool, q4_bool, sp_bool = True, True, True, True, True

q1_text = tk.Label(c, text="A, B, C, D, E, F", bg="grey")
q1_text.place(x=157.5-28, y=85+10)
q2_text = tk.Label(c, text="G, H, I, J, K, L", bg="grey")
q2_text.place(x=157.5-28+350, y=85+10)
q3_text = tk.Label(c, text="M, N, O, P, Q, R", bg="grey")
q3_text.place(x=157.5-28, y=85+10+230)
q4_text = tk.Label(c, text="S, T, U, V, W, X, Y, Z", bg="grey")
q4_text.place(x=157.5-28+330, y=85+10+230)

def make_sp():
    global sp, sp_bool
    if sp_bool:
        sp = c.create_rectangle(40+20,20+20,295+20+20,190+20,fill="red")
    master.after(33, unmake_sp)

def unmake_sp():
    c.delete(sp)
    master.after(33, make_sp) 

def make_q1():
    global q1, q1_bool
    if q1_bool:
        q1 = c.create_rectangle(40,20,295+20,190,fill="grey")
    master.after(33, unmake_q1)

def unmake_q1():
    c.delete(q1)
    master.after(33, make_q1)   

def make_q2():
    global q2, q2_bool
    if q2_bool:
        q2 = c.create_rectangle(20+275+90,20,295+275+90,190,fill="grey")
    master.after(50, unmake_q2)

def unmake_q2():
    c.delete(q2)
    master.after(50, make_q2)   

def make_q3():
    global q3, q3_bool
    if q3_bool:
        q3 = c.create_rectangle(40,50+200,295+20,220+200,fill="grey")
    master.after(75, unmake_q3)

def unmake_q3():
    c.delete(q3)
    master.after(75, make_q3)   

def make_q4():
    global q4, q4_bool
    if q4_bool:
        q4 = c.create_rectangle(20+275+90,50+200,295+275+90,220+200,fill="grey")
    master.after(100, unmake_q4)

def unmake_q4():
    c.delete(q4)
    master.after(100, make_q4)  


make_q1()
make_q2()
make_q3()
make_q4()
layer = 1
options = []
for i in range(0, 26):
    options.append(chr(65+i))
def next(quarter):
    global layer, q1_bool, q2_bool, q3_bool, q4_bool, options, overall_str, q1_text, q2_text, q3_text, q4_text
    start = 0
    end = 0
    if layer == 1:
        q4_bool = False
        if quarter == 1:
            start = 0
            end = 5
        elif quarter == 2:
            start = 6
            end = 11
        elif quarter == 3:
            start = 12
            end = 17
        else:
            start = 18
            end = 25
            q4_bool = True
        temp_options = []
        for i in range(start, end+1):
            temp_options.append(options[i])
        options = temp_options
    elif layer == 2:
        q4_bool = False
        q3_bool = False
        if quarter == 1:
            start = 0
            end = 1
        elif quarter == 2:
            start = 2
            end = 3
        elif quarter == 3:
            start = 4
            end = 5
        else:
            start = 6
            end = 7
        temp_options = []
        for a in range(start, end+1):
            temp_options.append(options[a])
        options = temp_options
    elif layer == 3:
        q1_bool, q2_bool, q3_bool, q4_bool = True, True, True, True
        if quarter == 1:
            overall_str += str(options[0])
        else:
            overall_str += str(options[1])
        txt.config(text=overall_str)
        layer = 0
        options = []
        for i in range(0, 26):
            options.append(chr(65+i))
    
    if len(options) <= 8 and len(options) > 2:
        q4_text.configure(text="", bg="black")
        t_i = [q1_text, q2_text, q3_text, q4_text]
        thres = int(len(options)/2)
        x = 0
        for k in range(thres):
            t_i[k].configure(text=options[x] + ", " + options[x+1], bg="grey")
            x += 2
    elif len(options) == 2:
        q1_text.configure(text=options[0], bg="grey")
        q2_text.configure(text=options[1], bg="grey")
        q3_text.configure(text="", bg="black")
        q4_text.configure(text="", bg="black")
    else:
        q1_text.configure(text="A, B, C, D, E, F", bg="grey")
        q2_text.configure(text="G, H, I, J, K, L", bg="grey")
        q3_text.configure(text="M, N, O, P, Q, R", bg="grey")
        q4_text.configure(text="S, T, U, V, W, X, Y, Z", bg="grey")


    layer += 1
    print(options)
    print(overall_str)

                

q1_b = tk.Button(master, text="q1", height=5, width=5, command= lambda: next(1))
q1_b.place(x=900, y = 20+50)
q2_b = tk.Button(master, text="q2", height=5, width=5, command= lambda: next(2))
q2_b.place(x=900, y = 170+50)
q3_b = tk.Button(master, text="q3", height=5, width=5, command= lambda: next(3))
q3_b.place(x=900, y = 320+50)
q4_b = tk.Button(master, text="q4", height=5, width=5, command= lambda: next(4))
q4_b.place(x=900, y = 470+50)




#lambda: layer_3(32, None)

def space():
    global overall_str, txt
    overall_str += " "
    print(overall_str)
    txt.config(text=overall_str)

def delete():
    global overall_str, txt
    overall_str = overall_str[:-1]
    txt.config(text=overall_str)

sp = tkinter.Button(master, text="Space", background='blue', height=3, width=30, command= lambda: space(), padx=10)
sp.place(x=170, y=600)
de = tkinter.Button(master, text="Delete", background='blue', height=3, width=30, command= lambda: delete(), padx=10)
de.place(x=530, y=600)




txt.place(relx=0.5, y=50, anchor="center")


master.configure(background='black')
master.mainloop()