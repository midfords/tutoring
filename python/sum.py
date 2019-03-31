
n = int( input("Enter a number. ") )

s = 0
for i in range(n + 1):
    s += i

print( "The sum from 1 to " + str(n) + " is " + str(s))