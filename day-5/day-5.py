# Day 5: Supply Stacks

# no surprise that i have to use the stack data structure here :) 

import re


'''
test input ...

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''

# a = open('input-day5.txt', 'r').read()
# a, b = a.split('\n\n')

# print(a.splitlines())


# manual method... definitely inefficient for large data sets
test_dict = {
	"list-1": ['Z', 'N'],
	"list-2": ['M', 'C', 'D'],
	"list-3": ['P']
}

x = open('day5-test-input.txt', 'r').read()

stacks, dirs = x.split('\n\n')


# each empty spot in a column is represented by 4 spaces
for line in stacks.splitlines():
	cur = line.split(' ')
	print(cur)





columns = stacks.splitlines()[-1].split(' ')
print('\n\n')
print(columns)


# identifying movements
for i in dirs.splitlines():
	a, b, c, d, e, f = i.split()
	b, d, f = int(b), int(d), int(f)
	# move b from d to f



