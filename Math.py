class Problem:
    """ This class encapsulates some interesting implementations with focus on: very simple - but hard to prove -
    mathematical problems and well known (classic) solutions for didactic problems """

    def __init__(self):
        pass

    @classmethod
    def collatz(cls, n) -> int:
        """ The hypothesis formulated In 1937 by the German mathematician Lothar Collatz: If the number is even,
        divide it by two, otherwise, multiply it by three and add one to it; In either case, repeat the same to the
        obtained result until the obtained result is equal to one.
            Args:
                n: An integer number greater than zero.
            Returns:
                The method return the number of steps until the function converges to 1. """
        count = 0
        while n != 1:
            count = count + 1
            if n % 2 == 0:
                # fast division by 2 with binary shift right
                n = n >> 1
            else:
                # using shift left to multiply (by two)
                p = n << 1
                n = p + n + 1
        return count


# Executing some tests
number = int(input("Give an input to the Collatz function: "))
print("The number {} took {} steps to converge to one".format(number, Problem.collatz(number)))
