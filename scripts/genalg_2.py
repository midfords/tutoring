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

		eq = ""
		num = random.randint(2, 4)
		for i in range(num):
			eq += genequation() + randomop()
		eq += genequation() + " = " + randnum()

		if eq.count("x") == 1:
			print(eq + "\n\n\n\n\t x = _______")
			count += 1

main()