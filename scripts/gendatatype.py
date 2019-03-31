import random

def genquestion():
	x = random.randint(0, 3)
	if (x == 0):
		return "\"" + str(genstring()) + "\""
	elif (x == 1):
		return str(genint())
	elif (x == 2):
		return str(genfloat())
	else:
		return str(genbool())

def genstring():
	s = ""
	for i in range(random.randint(1, 5)):
		if (random.randint(0, 1) == 1):
			s += chr(random.randint(48, 57))
		else:
			s += chr(random.randint(97, 122))
	return s

def genint():
	return random.randint(1, 100)

def genfloat():
	return random.random() * random.randint(0, 10)

def genbool():
	return random.randint(0, 1) == 1

def main():
	for i in range(100):
		print(genquestion() + "\t___ \n\n")

main()