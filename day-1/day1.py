

numbers = open('input-day-1.txt', 'r')

# test_nums = open('test-input-1.txt', 'r')

split_nums = numbers.read().split('\n\n')

double = [x.split('\n') for x in split_nums]
# print(double)
max_sum = 0
#highest = []
sums = []

for subarray in double:
	result = list(map(int, filter(lambda x: len(x) > 0, subarray)))
	total = sum(result)
	sums.append(total)
	if total > max_sum:
		max_sum = total
		#highest.append(max_sum)
		#print(result, max_sum)


top3 = sorted(sums)[-3:]
print(sum(top3))

print(max_sum)


# part 1 - 69289
# part 2 - 205615