from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class Todo:
    def __init__(self, tk):
        self.tk = tk
        self.tk.title("TO DO LIST")
        self.tk.iconbitmap("E:\PYTHON CODSOFT\TO-DO-LIST\main.ico.jpg")
        self.tk.geometry('650x500')

        self.label = Label(self.tk, text="TO-DO-LIST", font='ariel, 25 bold', width=12, bd=5, bg='light pink', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label1 = Label(self.tk, text="ADD TASK", font='ariel, 18 bold', width=12, bd=5, bg='light pink', fg='black')
        self.label1.place(x=40, y=54)

        self.label2 = Label(self.tk, text="TASKS", font='ariel, 18 bold', width=12, bd=5, bg='light pink', fg='black')
        self.label2.place(x=320, y=54)

        self.main_text = Listbox(self.tk, height=9, bd=5, width=23, font="ariel, 20 italic bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.tk, bd=5, height=2, width=30, font='ariel, 10 bold')
        self.text.place(x=20, y=120)

        #----------------------add task-----------------------#

        def add_task():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            self.text.delete(1.0, END)

        #----------------------delete task----------------------#

        def delete_task():
            selected_index = self.main_text.curselection()
            if selected_index:
                self.main_text.delete(selected_index)

        #----------------------edit task----------------------#

        def edit_task():
            selected_index = self.main_text.curselection()
            if selected_index:
                selected_task = self.main_text.get(selected_index)
                self.text.delete(1.0, END)
                self.text.insert(END, selected_task)

                def update_task():
                    new_content = self.text.get(1.0, END)
                    self.main_text.delete(selected_index)
                    self.main_text.insert(selected_index, new_content)
                    self.text.delete(1.0, END)
                    self.edit_window.destroy()

                def cancel_edit():
                    self.text.delete(1.0, END)
                    self.edit_window.destroy()

                self.edit_window = Toplevel(self.tk)
                self.edit_window.title("Edit Task")
                self.edit_window.geometry('300x150')

                edit_label = Label(self.edit_window, text="Edit Task", font='ariel, 18 bold', width=10, bd=5, bg='light pink', fg='black')
                edit_label.pack(side='top', fill=BOTH)

                edit_text = Text(self.edit_window, bd=5, height=2, width=30, font='ariel, 10 bold')
                edit_text.pack()

                edit_text.insert(END, selected_task)

                update_button = Button(self.edit_window, text="Update", font='sarif, 12 bold italic', width=10, bd=5, bg='pink', fg='black', command=update_task)
                update_button.pack(side='left', padx=10)

                cancel_button = Button(self.edit_window, text="Cancel", font='sarif, 12 bold italic', width=10, bd=5, bg='pink', fg='black', command=cancel_edit)
                cancel_button.pack(side='left', padx=10)

        def save_tasks():
            tasks = self.main_text.get(0, END)
            with open('task.txt', 'w') as file:
                for task in tasks:
                    file.write(task + '\n')

        self.button = Button(self.tk, text="ADD", font='sarif, 20 bold italic', width=10, bd=5, bg='pink', fg='black', command=add_task)
        self.button.place(x=30, y=180)

        self.button1 = Button(self.tk, text="DELETE", font='sarif, 20 bold italic', width=10, bd=5, bg='pink', fg='black', command=delete_task)
        self.button1.place(x=30, y=280)

        self.button2 = Button(self.tk, text="EDIT", font='sarif, 20 bold italic', width=10, bd=5, bg='pink', fg='black', command=edit_task)
        self.button2.place(x=30, y=380)

        with open('task.txt', 'r') as file:
            tasks = file.readlines()
            for task in tasks:
                self.main_text.insert(END, task.strip())

def main():
    tk = Tk()
    gui = Todo(tk)
    tk.mainloop()

if __name__ == "__main__":
    main()