import tkinter as tk
import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    
    dice1_image = tk.PhotoImage(file=f"dice{dice1}.png")
    dice2_image = tk.PhotoImage(file=f"dice{dice2}.png")
    dice3_image = tk.PhotoImage(file=f"dice{dice3}.png")
    
    label1.configure(image=dice1_image)
    label2.configure(image=dice2_image)
    label3.configure(image=dice3_image)
    label1.image = dice1_image
    label2.image = dice2_image
    label3.image = dice3_image
    
    number1.configure(text=f"Dado 1 : {dice1}")
    number2.configure(text=f"Dado 2 : {dice2}")
    number3.configure(text=f"Dado 3 : {dice3}")

root = tk.Tk()
root.title("Tira Dados")

label1 = tk.Label(root, image=None)
label2 = tk.Label(root, image=None)
label3 = tk.Label(root, image=None)

label1.pack(side="left")
label2.pack(side="left")
label3.pack(side="left")

number1 = tk.Label(root, text="", font=("Arial", 20))
number2 = tk.Label(root, text="", font=("Arial", 20))
number3 = tk.Label(root, text="", font=("Arial", 20))

number1.pack(side="left", padx=5)
number2.pack(side="left", padx=5)
number3.pack(side="left", padx=5)

button = tk.Button(root, text="Tirar dados", command=roll_dice)
button.pack()

root.mainloop()