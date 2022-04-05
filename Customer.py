class Customer:
    """ Abstracts the concept of a customer in the context of an on-line video streaming service """

    def __init__(self, name, phoneNumber, eMail, address):
        self.name = name
        self.phoneNumber = phoneNumber
        self.eMail = eMail
        self.address = address

    def toString(self):
        """ Provides with a string describing the values set to the fields of a particular instance of this class """
        print("Name: {} Phone: {} Address: {}".format(self.name, self.phoneNumber, self.address))
