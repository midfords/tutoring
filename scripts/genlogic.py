import random

def genequation(tf = True):
	x = random.randint(0, 1)
	if x == 0 and tf:
		return "True"
	else:
		return "False"

def randomlogic():
	x = random.randint(0, 1)
	if x == 0:
		return " and "
	else :
		return " or "

def main():
	for i in range(20):
		print(genequation() + randomlogic() + genequation() + randomlogic() + genequation() + randomlogic() + genequation() + "\t: \n")

main()