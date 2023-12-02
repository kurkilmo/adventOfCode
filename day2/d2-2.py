lines = open("data.txt").readlines()
sum = 0
for line in lines:
	line = line.strip()
	print(line)
	draws = line.split(":")[1].split(";")
	reds = []
	blues = []
	greens = []
	for draw in draws:
		spl = draw.split(",")
		for c in spl:
			try:
				count = int(c.split(" ")[1])

			except:
				count = 0
			if c.endswith("red"):
				reds.append(count)
			if c.endswith("green"):
                                greens.append(count)
			if c.endswith("blue"):
                                blues.append(count)
		print(f'red:{max(reds)} green:{max(greens)} blue:{max(blues)}')
		pwr = max(reds)+max(greens)*max(blues)
		print(pwr)
		sum = sum + pwr
print(f'sum: {sum}')
