# Day 3 - Rucksack Reorganization

# find letter that appears in both compartments (case sensitive)
# find letter's priority 
# sum priorities of duplicate objects 

from collections import Counter

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
badges = []


def find_priority(letter):
	return alphabet.index(letter) + 1

for g in groups:
	first, second, third = Counter(g[0]), Counter(g[1]), Counter(g[2])
	#print(first)
	intersection = first & second
	badge = intersection & third
	#print(list(badge))
	badges += list(badge)


#print(badges)
priorities = list(map(find_priority, badges))
print(sum(priorities))

	
				
		