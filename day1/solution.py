# Author Joshua Cox
import re

with open('d1data.txt') as file:
  data = file.readlines()

speltNumbersDict = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }

calibrationTotal1 = 0 # For Part 1
calibrationTotal2 = 0 # For Part 2

for line in data:
  numericNumbers = []
  speltNumbers = []

  for index, char in enumerate(line):
    if char.isdigit():
      numericNumbers.append((index, char))

  for speltNumber in speltNumbersDict:
    if re.search(speltNumber, line): # Checks if line contains that spelt number
      matches = list(re.finditer(speltNumber, line)) # Finds all matches of spelt number 
      speltNumbers.append((matches[0].start(), speltNumbersDict[speltNumber]))
      if len(matches) > 1:
        speltNumbers.append((matches[-1].span()[0], speltNumbersDict[speltNumber]))

  allNumbers = sorted(numericNumbers + speltNumbers, key = lambda x: x[0])

  if len(numericNumbers) > 0:
    calibrationTotal1 += int(numericNumbers[0][1] + numericNumbers[-1][1])
  if len(allNumbers) > 0:
    calibrationTotal2 += int(allNumbers[0][1] + allNumbers[-1][1])

print('Part 1:', calibrationTotal1)
print('Part 2:', calibrationTotal2)
