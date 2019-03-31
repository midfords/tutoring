import random

def gennum():
	return str(random.randint(0, 12))

def genop():
	x = random.randint(0, 2)
	if x == 0:
		return " + "
	elif x == 1:
		return " - "
	else:
		return " * "

def geneq():
	o = genop();
	x = random.randint(2, 3)
	top = " " + gennum() + "    " + gennum()
	if x > 2:
		top += "    " + gennum()
	mid = "---" + o + "---"
	if x > 2:
		mid += o + "---"
	bot = " " + gennum() + "    " + gennum()
	if x > 2:
		bot += "    " + gennum()

	return top + "\n" + mid + "\n" + bot

def main():
	for i in range(20):
		print(geneq() + "\t: \n")

main()