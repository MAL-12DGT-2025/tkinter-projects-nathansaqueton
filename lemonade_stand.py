import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import *

# Title
root = tk.Tk()
name = root.title("Lemonade Stand")

# Total price of lemonade
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

#Total price considering ice
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

def add_to_cart():
    numberp = number.get()
    choicep = choice.get()
    with_ice = ice_number.get()
    global cart
    global total_price
    if choicep == "1":
        if with_ice == "1":
            cart.append(f"{numberp} Lemonade(s), size: 100ml, with ice")
        else:
            cart.append(f"{numberp} Lemonade(s), size: 100ml")
    elif choicep == "2":
        if with_ice == "1":
            cart.append(f"{numberp} Lemonade(s), size: 250ml, with ice")
        else:
            cart.append(f"{numberp} Lemonade(s), size: 250ml")
    elif choicep == "3":
        if with_ice == "1":
            cart.append(f"{numberp} Lemonade(s), size: 500ml, with ice")
        else:
            cart.append(f"{numberp} Lemonade(s), size: 500ml")
    for i in range(len(cart)):
        cart_label.insert(END, cart[i])
        print(cart[i])
    #cart_label.config(text=f"Cart:\n {cart}")

# Variables
cart = []
total_price = 0
choice = tk.StringVar()
number = tk.StringVar()
ice_number = tk.StringVar()

# Widgets
image = PhotoImage(file="lemonade_pic.png")
resize_image = image.subsample(8, 8)
amount_of_lemonade = tk.Label(root, text="Amount of\nLemonade:")
image_label = ttk.Label(root, image=resize_image)
image_label.grid(row=0, column=0, rowspan=5)
amout_of_lemonade_box = ttk.Entry(root, textvariable = number)
size_text = tk.Label(root, text="Size:")
one_hundred_ml = ttk.Radiobutton(root, text="100ml", variable = choice, value=1, command= write_price)
two_hundred_fifty_ml = ttk.Radiobutton(root, text="250ml", variable = choice, value=2, command= write_price)
five_hundred_ml = ttk.Radiobutton(root, text="500ml", variable = choice, value=3, command= write_price)
with_ice = ttk.Checkbutton(root, text="With Ice", variable = ice_number, onvalue = 1, offvalue = 0, command= write_price)
one_hundred_ml_price = ttk.Label(root, text="$1.00")
two_hundred_fifty_ml_price = ttk.Label(root, text="$2.00")
five_hundred_ml_price = ttk.Label(root, text="$3.00")
cart_label = ttk.Label(root, text=f"Cart: {cart}")
total_price_label = ttk.Label(root, text=f"Total Price: {total_price}")
add_button = ttk.Button(root, text="Add to cart", command= add_to_cart)
ice_price = ttk.Label(root, text="$0.25")

# Grid
amount_of_lemonade.grid(row=0, column=1)
amout_of_lemonade_box.grid(row=0, column=2)
size_text.grid(row=1, column=1)
one_hundred_ml.grid(row=2, column=1)
two_hundred_fifty_ml.grid(row=3, column=1)
five_hundred_ml.grid(row=4, column=1)
with_ice.grid(row=5, column=1)
one_hundred_ml_price.grid(row=2, column=2)
two_hundred_fifty_ml_price.grid(row=3, column=2)
five_hundred_ml_price.grid(row=4, column=2)
cart_label.grid(row=7, column=0, pady=25)
total_price_label.grid(row=8, column=1, rowspan=2)
ice_price.grid(row=5, column=2)
add_button.grid(row=7, column=1, columnspan=2)

#Key biding
amount_of_lemonade.bind("<KeyRelease>", write_price)

root.mainloop()