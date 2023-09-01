from tkinter import * 
from tkinter import messagebox
from PIL import Image,ImageTk

class todo:
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

        self.text= Text(self.tk, bd=5, height=2, width=30, font='ariel, 10 bold')
        self.text.place(x=20, y=120)

        #----------------------add task-----------------------#

        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('task.txt', 'a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0,'end')

        #----------------------delete task----------------------#
        
        def delete():
            d = self.main_text.curselection()
            if d:
                look = self.main_text.get(d)
                with open('task.txt', 'r+') as f:
                    new = f.readlines()
                    f.seek(0)
                    for line in new:
                        item = str(look)
                        if item not in line:
                            f.write(line)
                    f.truncate()
                self.main_text.delete(d)

        with open('task.txt', 'r') as file:
            file.seek(0)
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
        file.close()

        def save():
            tasks = Listbox.get(0, tk.END)
            with open('task.txt', 'w') as file:
                for item in tasks:
                    file.write(item + '\n')
                

        self.button = Button(self.tk, text="ADD", font='sarif, 20 bold italic', width=10, bd=5, bg='pink', fg='black', command=add)
        self.button.place(x=30, y=180)

        self.button1 = Button(self.tk, text="DELETE", font='sarif, 20 bold italic', width=10, bd=5, bg='pink', fg='black', command=delete)
        self.button1.place(x=30, y=280)

        self.button2 = Button(self.tk, text="SAVE", font='sarif, 20 bold italic', width=10, bd=5, bg='pink', fg='black', command=save)
        self.button2.place(x=30, y=380)
        

        

def main():
    tk = Tk()
    gui = todo(tk)
    tk.mainloop()

if __name__ =="__main__":
    main()