data = open("d1data.txt")
lines = data.readlines()
sum = 0
for line in lines:
	digs = []
	for c in line:
		try:
			n = int(c)
		except:
			continue
		digs.append(n)
	cal = int(f'{digs[0]}{digs[-1]}')
	sum = sum + cal
	print(f'{line[0:-1]} | {cal}')
data.close()
print(f'sum: {sum}')
