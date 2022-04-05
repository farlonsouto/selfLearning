from Customer import *
from UserInterface import *

customer = Customer("Farlon", "12345678", "my.email@provider.com", "Ola Nordman Gt 123")
customer.toString()

guiRoot = tk.Tk()
gui = UserInterface(guiRoot)
guiRoot.title("Streaming App")
guiRoot.geometry("640x480")
guiRoot.mainloop()

