import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(password_length))
    password_label.config(text="Generated Password: " + password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry('650x500')

# Create and pack the widgets
length_label = tk.Label(window, text="Password Length:", font='ariel, 25 bold', width=18, bd=2, bg='light pink', fg='black')
length_label.place(x=150, y=5)

length_entry = tk.Entry(window,font='ariel, 15',width=10)
length_entry.place(x=225, y=52)

generate_button = tk.Button(window, text="Generate", command=generate_password, font='ariel, 10 bold', width=10, bd=2, bg='light pink', fg='black')
generate_button.place(x=225, y=90)

password_label = tk.Label(window, text="Generated Password:", font='ariel, 15', bg='light blue', fg='black')
password_label.place(x=150,y=140)

# Start the main loop
window.mainloop()