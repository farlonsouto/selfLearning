import tkinter as tk


class UserInterface:
    """ Abstraction of a simple user interface for learning purposes """

    def __init__(self, guiRoot):
        """Connects to the next available port.
        Args:
            guiRoot: Injects a Tekinter instance.
        """
        self.username = tk.StringVar()
        self.guiRoot = guiRoot
        self.initGui()

    def executeAction(self):
        """Prints out the username. """
        print("The username is {}".format(self.username.get()))

    def initGui(self):
        """Instantiates the GUI."""
        tk.Label(self.guiRoot, text="Enter a username:").pack()
        tk.Entry(self.guiRoot, textvariable=self.username).pack()
        tk.Button(self.guiRoot, text="Action", command=self.executeAction).pack()


