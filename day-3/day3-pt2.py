# Day 3 - Rucksack Reorganization

# find letter that appears in both compartments (case sensitive)
# find letter's priority 
# sum priorities of duplicate objects 

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# lowercase a-z - 1-26
# uppercase A-Z - 27-52


input1 = open('test-input-day3.txt', 'r')
# separate into three line groups

lines = input1.read().split('\n')


#print(lines)

def divide_groups(l, n):
	for i in range(0, len(l), n):
		yield l[i:i + n]


groups = list(divide_groups(lines, 3))

for g in groups:
	print(g)