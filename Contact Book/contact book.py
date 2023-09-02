from tkinter import *
from tkinter import messagebox


class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x400")

        self.contacts = []

        self.name_label = Label(self.root, text="Name:", bg="lavender", font='ariel, 18', width=18)
        self.name_label.place(x=650, y=5)

        self.name_entry = Entry(self.root, bg="#d8bfd8", width=20, font='ariel, 18')
        self.name_entry.place(x=650, y=40)

        self.phone_label = Label(self.root, text="Phone:", bg="lavender", font='ariel, 18', width=18)
        self.phone_label.place(x=650, y=70+5)

        self.phone_entry = Entry(self.root, bg="#d8bfd8",  width=20, font='ariel, 18')
        self.phone_entry.place(x=650, y=100+10)

        self.email_label = Label(self.root, text="Email:", bg="lavender", font='ariel, 18', width=18)
        self.email_label.place(x=650, y=130+15)

        self.email_entry = Entry(self.root, bg="#d8bfd8",  width=20, font='ariel, 18')
        self.email_entry.place(x=650, y=160+20)

        self.address_label = Label(self.root, text="Address:", bg="lavender", font='ariel, 18', width=18)
        self.address_label.place(x=650, y=190+25)

        self.address_entry = Entry(self.root, bg="#d8bfd8",  width=20, font='ariel, 18')
        self.address_entry.place(x=650, y=220+30)

        self.add_button = Button(self.root, text="Add Contact", command=self.add_contact, bg="light blue", width=36)
        self.add_button.place(x=650, y=250+35)

        self.view_button = Button(self.root, text="View Contacts", command=self.view_contacts, bg="light blue", width=36)
        self.view_button.place(x=650, y=280+40)

        self.search_button = Button(self.root, text="Search Contact", command=self.search_contact, bg="light blue", width=36)
        self.search_button.place(x=650, y=310+45)

        self.update_button = Button(self.root, text="Update Contact", command=self.update_contact, bg="light blue", width=36)
        self.update_button.place(x=650, y=340+50)

        self.delete_button = Button(self.root, text="Delete Contact", command=self.delete_contact, bg="light blue", width=36)
        self.delete_button.place(x=650, y=370+55)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone and email and address:
            contact = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }
            self.contacts.append(contact)
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("No Contacts", "No contacts available.")

    def search_contact(self):
        name = self.name_entry.get()
        if name:
            found_contacts = [contact for contact in self.contacts if contact['name'].lower() == name.lower()]
            if found_contacts:
                contact_list = "\n".join([f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n" for contact in found_contacts])
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("No Results", "No contacts found.")
        else:
            messagebox.showerror("Error", "Please enter a name to search.")

    def update_contact(self):
        name = self.name_entry.get()
        if name:
            for contact in self.contacts:
                if contact['name'].lower() == name.lower():
                    contact['phone'] = self.phone_entry.get()
                    contact['email'] = self.email_entry.get()
                    contact['address'] = self.address_entry.get()

                    messagebox.showinfo("Success", "Contact updated successfully.")
                    self.clear_entries()
                    return
            messagebox.showinfo("No Contact", "Contact not found.")
        else:
            messagebox.showerror("Error", "Please enter a name to update.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name:
            for contact in self.contacts:
                if contact['name'].lower() == name.lower():
                    self.contacts.remove(contact)
                    messagebox.showinfo("Success", "Contact deleted successfully.")
                    self.clear_entries()
                    return
            messagebox.showinfo("No Contact", "Contact not found.")
        else:
            messagebox.showerror("Error", "Please enter a name to delete.")

    def clear_entries(self):
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.address_entry.delete(0, END)

root = Tk()
contact_book = ContactBook(root)
root.mainloop()