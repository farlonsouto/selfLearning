import tkinter as tk


class UserInterface:

    def __init__(self, root):
        self.root = root
        self.make_gui()

    def executeAction(self):
        print("Action executed")

    def make_gui(self):
        label = tk.Label(self.root, text="Hello There").pack()
        btn = tk.Button(self.root, text="Action", command=self.executeAction).pack()


root = tk.Tk()
gui = UserInterface(root)
root.title("Streaming App")
root.geometry("640x480")
root.mainloop()
