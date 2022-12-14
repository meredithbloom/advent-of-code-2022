# rock, paper, scissors

'''
A - rock
B - paper
C - scissors

X - rock - 1 pt
Y - paper - 2 pts
Z - scissors - 3 pts

round outcome -
loss - 0 pts
draw - 3 pts
win - 6 pts
''' 

#input = open('test-input-day2.txt', 'r')
input = open('input-day-2.txt', 'r')
rounds = input.read().split('\n')
#print(rounds)

opp_combos = [('A','Z'), ('B','X'), ('C','Y')]

player_combos = [('C','X'), ('A', 'Y'), ('B', 'Z')]

draws = [('A','X'), ('B','Y'), ('C','Z')]

point_vals = {
	'X': 1,
	'Y': 2,
	'Z': 3
}

total_pts = 0

for pair in rounds:
	moves = tuple(pair.split())
	try:
		move_pts = point_vals[moves[1]]
	except IndexError:
		print(moves)
		break
	round_pts = move_pts
	if moves in opp_combos:
		round_pts += 0
	elif moves in player_combos:
		round_pts += 6
	elif moves in draws:
		round_pts += 3
	total_pts += round_pts

print(total_pts)

# part 1 - 13502