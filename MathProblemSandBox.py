from MathProblem import MathProblem

number = int(input("Give an input to the Collatz function: "))
print("The number {} took {} steps to converge to one".format(number, MathProblem.collatz(number)))

steps = int(input("Give a limit to the Harmonic Series function: "))
print("The harmonic series sum up with {} steps is: {}".format(steps, MathProblem.harmonicSeries(steps)))

listOfNumbers = []
value = ""
print("Provide integer input values to build a list so we can sort it. Enter 'x' to finish.")
while True:
    value = input("Add a value to the list: ")
    if value == "x":
        break
    else:
        listOfNumbers.append(int(value))
MathProblem.bubbleSort(listOfNumbers)
print(listOfNumbers)