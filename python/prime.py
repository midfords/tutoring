
def isDivisable(n, m):
    return n % m == 0

def getDivisableList(n):
    d = []

    for i in range(1, n+1):
        if isDivisable(n, i):
            d.append(i)

    return d

def userInput():
    while True:
        try:
            c = input("Enter a number ('q' to quit): ")

            if c == 'q':
                return 'q'

            return int(c)
        except:
            print("Error. Enter a number or 'q'")

def printList(l):
    if len(l) > 0:
        print(str(l[0]), end="")

    for i in range(1, len(l)):
        print(", " + str(l[i]), end="")

def main():

    c = userInput()
    while c != 'q':
        d = getDivisableList(c)

        print("Numer is divisable by: ", end="")
        printList(d)
        print()

        if len(d) <= 2:
            print("Number is prime!")
        else:
            print("Number is not prime.")

        c = userInput()


main()

print("Program exited successfully")