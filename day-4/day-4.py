# Day 4: Camp Cleanup

# long list of pairs of section assignments
# need to compare ranges of section assignments to see if there is overlap
# only need to identify those assignment pairs where one range completely contains the other range


input1 = open('day4-test-input.txt')


pairs = input1.read().split('\n')

#print(pairs)

for pair in pairs:
	sections = pair.split(',')
	print(sections)