import tkinter as tk
from tkinter import ttk

def converter(event):
    num = int(number.get())
    if converted.get() == 1:
        result = (num * 9/5) + 32
        result_L.config(text = f"{num}C is equal to {result}F")

    elif converted.get() == 2:
        result = (num - 32) * 5/9
        result_L.config(text = f"{num}F is equal to {result}C")

root = tk.Tk()
converted = tk.IntVar(value=1)

name = root.title("Temperature Converter")

title = ttk.Label(root, text="Temperature Converter")
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


number = ttk.Entry(root)
number.grid(row=1, column=0, columnspan=2)

c_to_f = ttk.Radiobutton(root, text="Celsius to Fahrenheit", value=1, variable = converted)
c_to_f.grid(row=2, column=0)

f_to_c = ttk.Radiobutton(root, text="Fahrenheit to Celsius", value=2, variable = converted)
f_to_c.grid(row=2, column=1)

convert = ttk.Button(root, text="Convert", command=converter)
convert.grid(row=3, column=0, columnspan=2)

result_L = ttk.Label(root, text="")
result_L.grid(row=4, column=0, columnspan=2)

root.bind("<Return>", converter)


root.mainloop()