import tkinter as tk
from tkinter import ttk
import random as rand

choice_list = ["Rock", "Paper", "Scissors"]

user_score = 0

def button_click(event):
    global user_score
    computer_choice = rand.choice(choice_list)
    if event == computer_choice:
        result = "It's a tie!"
        subheading.config(text=result)
    elif event == "Rock" and computer_choice == "Scissors":
        win()
        user_score = user_score + 1
        score.config(text=f"Score: {user_score}")
    elif event == "Rock" and computer_choice == "Paper":
        lose()
    elif event == "Paper" and computer_choice == "Rock":
        win()
        score.config(text=f"Score: {user_score}")
        user_score = user_score + 1
    elif event == "Paper" and computer_choice == "Scissors":
        lose()
    elif event == "Scissors" and computer_choice == "Paper":
        win()
        user_score = user_score + 1
        score.config(text=f"Score: {user_score}")
    elif event == "Scissors" and computer_choice == "Rock":
        lose()
    
def win():
    result = "You Win!"
    subheading.config(text=result)

def lose():
    result = "You Lose!"
    subheading.config(text=result)

root = tk.Tk()
root.title("Rock Paper Scissors")

title = tk.Label(root, text="Rock Paper \nScissors Game")
title.grid(row=0, column=1) 

subheading = tk.Label(root, text="Make your choice")
subheading.grid(row=1, column=1)

choice = tk.StringVar()

score = tk.Label(root, text=f"Score: {user_score}")
score.grid(row=2, column=1)

rock = ttk.Button(root, text="Rock", command = lambda:button_click("Rock"))
rock.grid(row=3, column=0)

paper = ttk.Button(root, text="Paper", command = lambda:button_click("Paper"))
paper.grid(row=3, column=1)

scissors = ttk.Button(root, text="Scissors", command = lambda:button_click("Scissors"))
scissors.grid(row=3, column=2)

root.mainloop()
