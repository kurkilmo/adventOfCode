d = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 8}
sum = 0
lines = open("d1data.txt").readlines()
for line in lines:
	digs = []
	for i in range(len(line)):
		try:
			digs.append(int(line[i]))
			continue
		except:
			pass
		for j in range(5):
			s = line[i:i+j+1]
			try:
				dig = d[s]
				digs.append(dig)
				break
			except:
				pass
	num = digs[0] * 10 + digs[-1]
	sum = sum + num
	print(f'{line} | {num}')
print(f'sum: {sum}')
