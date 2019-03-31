

import random

def randomop():
	x = random.randint(0, 3)
	if x == 0:
		return " + "
	elif x == 1 :
		return " - "
	elif x == 2 :
		return " / "
	else :
		return " * "

def randnum():
	return str(random.randint(0, 10))

def main():
	for i in range(50):
		eq = ""
		num = random.randint(2, 4)
		for i in range(num):
			eq += randnum() + randomop()
		eq += randnum() + " = \t________ \n"

		print(eq)
main()