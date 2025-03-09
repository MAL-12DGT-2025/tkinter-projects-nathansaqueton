import tkinter as tk
from tkinter import ttk

root = tk.Tk()
name = root.title("Calculator")

def on_click(button):
    current = equation.get()
    current = current + button
    equation.set(current)

def clear():
    equation.set("")

def calculate():
    try:
        result = eval(equation.get())
        equation.set(result)
    except:
        equation.set("Error")

equation = tk.StringVar()

display_w = ttk.Entry(root, textvariable=equation)
display_w.grid(row=0, column=0, columnspan=4)

button_7 = ttk.Button(root, text="7", command = lambda:on_click("7"))
button_7.grid(row=1, column=0)

button_8 = ttk.Button(root, text="8", command = lambda:on_click("8"))
button_8.grid(row=1, column=1)

button_9 = ttk.Button(root, text="9", command = lambda:on_click("9"))
button_9.grid(row=1, column=2)

button_div = ttk.Button(root, text="/", command = lambda:on_click("/"))
button_div.grid(row=1, column=3)

button_4 = ttk.Button(root, text="4", command = lambda:on_click("4"))
button_4.grid(row=2, column=0)

button_5 = ttk.Button(root, text="5", command = lambda:on_click("5"))
button_5.grid(row=2, column=1)

button_6 = ttk.Button(root, text="6", command = lambda:on_click("6"))
button_6.grid(row=2, column=2)

button_mul = ttk.Button(root, text="*", command = lambda:on_click("*"))
button_mul.grid(row=2, column=3)

button_1 = ttk.Button(root, text="1", command = lambda:on_click("1"))
button_1.grid(row=3, column=0)

button_2 = ttk.Button(root, text="2", command = lambda:on_click("2"))
button_2.grid(row=3, column=1)

button_3 = ttk.Button(root, text="3", command = lambda:on_click("3"))
button_3.grid(row=3, column=2)

button_sub = ttk.Button(root, text="-", command = lambda:on_click("-"))
button_sub.grid(row=3, column=3)

button_CLR = ttk.Button(root, text="CLR", command = clear)
button_CLR.grid(row=4, column=0)

button_0 = ttk.Button(root, text="0", command = lambda:on_click("0"))
button_0.grid(row=4, column=1)

button_equal = ttk.Button(root, text="=", command = calculate)
button_equal.grid(row=4, column=2)

button_add = ttk.Button(root, text="+", command = lambda:on_click("+"))
button_add.grid(row=4, column=3)

root.mainloop()