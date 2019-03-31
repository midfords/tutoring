

print("Right Triangles!")

a = input("What is a? (leave blank for unknown) ")
b = input("What is b? (leave blank for unknown) ")
c = input("What is c? (leave blank for unknown) ")

##  a^2 + b^2 = c^2

if a == "":
	c = int(c)
	b = int(b)
	a = math.sqrt((c**2) - (b**2))
	print("a = " + str(a))

elif b == "":
	c = int(c)
	a = int(a)
	b = math.sqrt((c**2) - (a**2))
	print("b = " + str(b))

elif c == "":
	a = int(a)
	b = int(b)
	c = math.sqrt((a**2) + (b**2))
	print("c = " + str(c))

else:
	a = int(a)
	b = int(b)
	c = int(c)
	d = math.sqrt((a**2) + (b**2))
	if d == c:
		print("The right triangle is valid!")
	else:
		print("The right triangle is not valid!")

