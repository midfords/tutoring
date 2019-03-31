import random

def printDice(n):
	if n==0:
		print("""+-------+
|       |
|   o   |
|       |
+-------+""")
	elif n==1:
		print("""+-------+
|     o |
|       |
| o     |
+-------+""")
	elif n==2:
		print("""+-------+
|     o |
|   o   |
| o     |
+-------+""")
	elif n==3:
		print("""+-------+
| o   o |
|       |
| o   o |
+-------+""")
	elif n==4:
		print("""+-------+
| o   o |
|   o   |
| o   o |
+-------+""")
	else:
		print("""+-------+
| o   o |
| o   o |
| o   o |
+-------+""")


def main():
	c = 'y'
	while c == 'y':
		i = random.randint(0, 5)
		printDice(i)
		i = random.randint(0, 5)
		printDice(i)

		c = input("Roll again? (y/n)")

main()

print("Program exited successfully.")
