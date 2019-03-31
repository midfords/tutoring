

import random

def genequation():
	x = random.randint(0, 1)
	if x == 0:
		return randnum()
	else:
		return "x"

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
	count = 0
	while count < 50:
		eq = genequation() + randomop() + genequation() + " = " + randnum() + "\t: ________ \n"

		if eq.count("x") == 1:
			print(eq)
			count += 1

main()