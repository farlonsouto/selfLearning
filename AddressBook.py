import tkinter as tk


class AddressBook:
    """ Abstracts a simple address book for learning purposes"""

    def __init__(self, gui):
        """ Creates a new AddressBook and creates a file named addressBook.csv
            if one does not exist yet"""
        with open("addressBook.csv", "a") as file:
            file.close()
        self.createGui(gui)

    def saveAddress(self):
        """ Persists the address informed by user in the UI into the file addressBook.csv """
        record = self.address.get()
        if len(record) > 0:
            with open("addressBook.csv", "a") as file:
                file.write(record + str('\n'))
            file.close()
        else:
            print("Empty address informed: Ignored.")

    def createGui(self, gui):
        """ Defines the GUI with its labels, input fields and buttons """
        tk.Label(gui, text="Type your address").grid(row=1, column=1)
        self.address = tk.StringVar()
        tk.Entry(gui, textvariable=self.address).grid(row=1, column=2)
        tk.Button(gui, text="Save Address", command=self.saveAddress).grid(row=1, column=3)


root = tk.Tk()
addressBook = AddressBook(root)
root.title("Address Book")
root.geometry("640x480")
root.mainloop()
