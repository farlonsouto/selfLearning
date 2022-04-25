# Functions as dictionary values and exception handling
def handle_A(base) -> str:
    if base == "A":
        return "G"
    else:
        return "A"


def handle_T(base) -> str:
    if base == "T":
        return "U"
    else:
        return "T"


handle = {"A": handle_A, "a": handle_A, "T": handle_T, "t": handle_T}

inputString = input("Provide an input: ")

transformed = []

# using a simple for loop
for symbol in inputString:
    try:
        transformed.append(handle[symbol](symbol))
    except (KeyError, TypeError):
        print("Cannot handle symbol {}".format(symbol))
print(transformed)

# using comprehensions
transformed = []
try:
    transformed = [handle[s](s) for s in inputString]
except (KeyError, TypeError):
    print("Cannot handle a symbol")

print(transformed)
