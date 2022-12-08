# Day 3 - Rucksack Reorganization

# find letter that appears in both compartments (case sensitive)
# find letter's priority 
# sum priorities of duplicate objects 

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# lowercase a-z - 1-26
# uppercase A-Z - 27-52


#input1 = open('test-input-day3.txt', 'r')
input1 = open('input-day3.txt')

rucksacks = input1.read().split('\n')

sum = 0

for r in rucksacks:
	length = len(r)
	halfway = length/2
	half1, half2 = r[:int(halfway)], r[int(halfway):]
	# print(half1)
	# print(half2)
	# print()
	temp_dict = {}
	for letter in half1:
		if letter in temp_dict:
			temp_dict[letter] += 1
		else:
			temp_dict[letter] = 1
	for letter in half2:
		if letter in temp_dict:
			#print(letter)
			priority = alphabet.index(letter) + 1
			sum += priority 
			break;

print(sum)