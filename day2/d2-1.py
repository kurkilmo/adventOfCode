lines = open("data.txt").readlines()
rmax = 12
gmax = 13
bmax = 14
sum = 0
for line in lines:
	line = line.strip()
	print(line)
	id = int(line.split(":")[0][4:])
	draws = line.split(":")[1].split(";")
	possible = True
	for draw in draws:
		spl = draw.split(",")
		r = 0
		g = 0
		b = 0
		for c in spl:
			try:
				count = int(c.split(" ")[1])

			except:
				count = 0
			if c.endswith("red"):
				r = count
			if c.endswith("green"):
                                g = count
			if c.endswith("blue"):
                                b = count
		print(f'red:{r}, green:{g}, blue: {b}')
		if (r > rmax) | (g > gmax) | (b > bmax):
			possible = False
	if possible:
		print("VALID")
		sum = sum + id
print(f'sum: {sum}')
