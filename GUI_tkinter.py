import tkinter as tk
from tkinter import Tk, Button, Text, END

top = Tk()
top.geometry("180x600")
answer = Text(width=160, height=5)
answer.place(x=0, y=65)

def show(x):
    try:
        if x == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.insert(tk.INSERT, x)
            answer.insert(tk.INSERT, final_answer)

        else:
            answer.insert(tk.INSERT, x)
    except:
        answer.delete(1.0, END)

B1 = Button(top, text="1", width = 10, height = 5, command = lambda: show("1"))
B1.place(x=0, y=170)

B2 = Button(top, text="2", width = 10, height = 5, command = lambda: show("2"))
B2.place(x=80, y=170)

B3 = Button(top, text="3", width = 10, height = 5, command = lambda: show("3"))
B3.place(x=160, y=170)

B4 = Button(top, text="4", width = 10, height = 5, command = lambda: show("4"))
B4.place(x=0, y=255)

B5 = Button(top, text="5", width = 10, height = 5, command = lambda: show("5"))
B5.place(x=80, y=255)

B6 = Button(top, text="6", width = 10, height = 5, command = lambda: show("6"))
B6.place(x=160, y=255)

B7 = Button(top, text="7", width = 10, height = 5, command = lambda: show("7"))
B7.place(x=0, y=340)

B8 = Button(top, text="8", width = 10, height = 5, command = lambda: show("8"))
B8.place(x=80, y=340)

B9 = Button(top, text="9", width = 10, height = 5, command = lambda: show("9"))
B9.place(x=160, y=340)

B0 = Button(top, text="0", width = 10, height = 5, command = lambda: show("0"))
B0.place(x=0, y=425)

Bpl = Button(top, text="+", width = 10, height = 5, command = lambda: show("+"))
Bpl.place(x=80, y=425)

Be = Button(top, text="=", width = 10, height = 5, command = lambda: show("="))
Be.place(x=160, y=425)
top.mainloop()