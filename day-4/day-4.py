# Day 4: Camp Cleanup

# long list of pairs of section assignments
# need to compare ranges of section assignments to see if there is overlap
# only need to identify those assignment pairs where one range completely contains the other range


#input1 = open('day4-test-input.txt')

input1 = open('day-4-input.txt')

pairs = input1.read().split('\n')

#print(pairs)
redundancy_count = 0
no_overlap = 0
overlap = 0

print(f'there are {len(pairs)} total pairs of elves')

for pair in pairs:
	sections = pair.split(',')
	ranges = []
	for s in sections:
		try:
			ranges.append(tuple(map(int, s.split('-'))))
		except ValueError:
			break;
	#print(ranges)
	if len(ranges) == 0:
		break;
	b1, b2 = ranges[0][0], ranges[1][0]
	#print(b1,b2)
	t1, t2 = ranges[0][1], ranges[1][1]
	#print(t1, t2)
	# if ranges don't touch at all we can move on
	if (t1 < b2) or (t2 < b1):
		no_overlap += 1
		#print('no overlap')
	elif (b1>=b2) and (t1<=t2):
		redundancy_count += 1
		overlap += 1
		#print(b2,t2, ' contains ', b1,t1)
	elif (b1<=b2) and (t1>=t2):
		redundancy_count += 1
		overlap += 1
	else:
		overlap += 1
		#print(b1,t1, ' contains ', b2,t2)
#print(redundancy_count)
print(overlap)

