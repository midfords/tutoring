
def isDivisibleByThreeOrFive(n):
    return n % 3 == 0 or n % 5 == 0


n = int(input("enter number "))

s = 0
for i in range(1, n+1):
    if isDivisibleByThreeOrFive(i):
        s += i

print(s)