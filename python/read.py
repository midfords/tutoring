import sys

path = ""
if len(sys.argv) <= 1:
    path = input("Enter file path. ")
else:
    path = sys.argv[1]

file = open(path, 'r')

lines = file.readlines()

count = 1
for l in lines:
    print(str(count) + "\t", end="")
    print(l, end="")
    count += 1
