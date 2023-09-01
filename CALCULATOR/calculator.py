import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from PIL import Image,ImageTk

#-------------------CREATING BUTTONS--------------------
def click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

r = tk.Tk()
r.title("Calculator")

entry = tk.Entry(r, width=20, font=("Arial", 14),bg='black', fg='white')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("+", 4, 3)
]

for button_text, row, column in buttons:
    button = tk.Button(r, text=button_text, width=5, height=2, font=("Arial", 12),bg='light yellow', fg='black', command=lambda text=button_text: click(text))
    button.grid(row=row, column=column, padx=5, pady=5)

button_clear = tk.Button(r, text="C", width=5, height=2, font=("Arial", 12),bg='light pink', fg='black', command=clear)
button_clear.grid(row=5, column=0, padx=5, pady=5)

button_equal = tk.Button(r, text="=", width=5, height=2, font=("Arial", 12), bg='light blue', fg='black', command=equal)
button_equal.grid(row=4, column=2, padx=5, pady=5)

r.mainloop()