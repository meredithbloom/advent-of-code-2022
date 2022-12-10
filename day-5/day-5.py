# Day 5: Supply Stacks

# no surprise that i have to use the stack data structure here :) 

#import re


'''
test input ...

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 


'''

# manual method... definitely inefficient for large data sets
test_dict = {
	"list-1": ['Z', 'N'],
	"list-2": ['M', 'C', 'D'],
	"list-3": ['P']
}


x = open('day5-test-input.txt', 'r').read()


x, y = x.split('\n\n')

# x,y = x.splitlines(), y.splitlines()

print(x)
print()
print(y)

