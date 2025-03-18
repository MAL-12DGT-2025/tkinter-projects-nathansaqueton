import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

root = tk.Tk()
name = root.title("Lemonade Stand")

total_price = 0
choice = tk.StringVar()
number = tk.StringVar()
ice_number = tk.StringVar()
placeholder = tk.StringVar()

#def lemonade_order():
#    global number
#    calculate_price()

def write_price():
    global total_price
    choicep = choice.get()
    numberp = number.get()
    if choicep == "1":
        total_price = eval(f"{numberp}*1")
        ice_calulation()
    elif choicep == "2":
        total_price = eval(f"{numberp}*2")
        ice_calulation()
    elif choicep == "3":
        total_price = eval(f"{numberp}*3")
        ice_calulation()
    else:
        total_price = 0

def ice_calulation():
    global total_price
    with_ice = ice_number.get()
    numberpp = number.get()
    if with_ice == "1":
        total_price = eval(f"{total_price}+({numberpp}*0.25)")
        total_price_label.config(text=f"Total Price: {total_price}")
    elif with_ice == "0":
        total_price = total_price
        total_price_label.config(text=f"Total Price: {total_price}")
    else:
        total_price = total_price
        total_price_label.config(text=f"Total Price: {total_price}")

image = PhotoImage(file="lemonade_pic.png")
resize_image = image.subsample(8, 8)
image_label = ttk.Label(root, image=resize_image)
image_label.grid(row=0, column=0, rowspan=5)

amount_of_lemonade = tk.Label(root, text="Amount of\nLemonade:")
amount_of_lemonade.grid(row=0, column=1)

amout_of_lemonade_box = ttk.Entry(root, textvariable = number)
amout_of_lemonade_box.grid(row=0, column=2)

size_text = tk.Label(root, text="Size:")
size_text.grid(row=1, column=1)

one_hundred_ml = ttk.Radiobutton(root, text="100ml", variable = choice, value=1, command= write_price)
one_hundred_ml.grid(row=2, column=1)

two_hundred_fifty_ml = ttk.Radiobutton(root, text="250ml", variable = choice, value=2, command= write_price)
two_hundred_fifty_ml.grid(row=3, column=1)

five_hundred_ml = ttk.Radiobutton(root, text="500ml", variable = choice, value=3, command= write_price)
five_hundred_ml.grid(row=4, column=1)

with_ice = ttk.Checkbutton(root, text="With Ice", variable = ice_number, onvalue = 1, offvalue = 0, command= write_price)
with_ice.grid(row=5, column=1)

one_hundred_ml_price = ttk.Label(root, text="$1.00")
one_hundred_ml_price.grid(row=2, column=2)

two_hundred_fifty_ml_price = ttk.Label(root, text="$2.00")
two_hundred_fifty_ml_price.grid(row=3, column=2)

five_hundred_ml_price = ttk.Label(root, text="$3.00")
five_hundred_ml_price.grid(row=4, column=2)

total_price_label = ttk.Label(root, text=f"Total Price: {total_price}")
total_price_label.grid(row=6, column=0)

ice_price = ttk.Label(root, text="$0.25")
ice_price.grid(row=5, column=2)

pay_button = ttk.Button(root, text="Pay")
pay_button.grid(row=6, column=1, columnspan=2)

amount_of_lemonade.bind("<KeyRelease>", write_price)

root.mainloop()