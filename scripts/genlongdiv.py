
import random

def main():
	for i in range(50):
		num = random.randint(0, 70)
		num2 = num * random.randint(0, 20) + random.randint(0, num)

		print("\n\n\n\n    ______\n" + str(num) + " | " + str(num2) + "\n")

main()