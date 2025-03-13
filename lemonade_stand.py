import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

root = tk.Tk()
name = root.title("Lemonade Stand")

image = PhotoImage(file="test_image.png")
image_label = ttk.Label(root, image=image)
image_label.grid(row=0, column=0)


amount_of_lemonade = tk.Label(root, text="Amount of\nLemonade:")
amount_of_lemonade.grid(row=0, column=1)

amout_of_lemonade_box = ttk.Entry(root)
amout_of_lemonade_box.grid(row=0, column=2)

size_text = tk.Label(root, text="Size:")
size_text.grid(row=1, column=1)

one_hundred_ml = ttk.Radiobutton(root, text="100ml")
one_hundred_ml.grid(row=2, column=1)

two_hundred_fifty_ml = ttk.Radiobutton(root, text="250ml")
two_hundred_fifty_ml.grid(row=3, column=1)

five_hundred_ml = ttk.Radiobutton(root, text="500ml")
five_hundred_ml.grid(row=4, column=1)

with_ice = ttk.Checkbutton(root, text="With Ice")
with_ice.grid(row=5, column=1)

one_hundred_ml_price = ttk.Label(root, text="$1.00")
one_hundred_ml_price.grid(row=2, column=2)

two_hundred_fifty_ml_price = ttk.Label(root, text="$2.00")
two_hundred_fifty_ml_price.grid(row=3, column=2)

five_hundred_ml_price = ttk.Label(root, text="$3.00")
five_hundred_ml_price.grid(row=4, column=2)

root.mainloop()