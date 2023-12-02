lines = open("data.txt").readlines()
sum = 0
for line in lines:
	line = line.strip()
	print(line)
	draws = line.split(":")[1].split(";")
	reds = 0
	blues = 0
	greens = 0
	for draw in draws:
		spl = draw.split(",")
		for c in spl:
			try:
				count = int(c.split(" ")[1])
			except:
				count = 0
			if c.endswith("red"):
				if count > reds:
					reds = count
			if c.endswith("green"):
				if count > greens:
					greens = count
			if c.endswith("blue"):
				if count > blues:
					blues = count
	print(f'red:{reds} green:{greens} blue:{blues}')
	pwr = reds*greens*blues
	print(pwr)
	sum = sum + pwr
print(f'sum: {sum}')
