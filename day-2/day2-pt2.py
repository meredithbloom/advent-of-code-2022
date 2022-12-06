# rock, paper, scissors

'''
A - rock - 1pt
B - paper - 2pts
C - scissors - 3pts

X - lose - 0 pts
Y - tie - 3 pts
Z - win - 6 pts

round outcome -
loss - 0 pts
draw - 3 pts
win - 6 pts
''' 

p_wins = {
	'A': 'B',
	'B': 'C',
	'C': 'A'
}

ties = {
	'A': 'A',
	'B': 'B',
	'C': 'C'
}

p_loses = {
	'A': 'C',
	'B': 'A',
	'C': 'B'
}

point_vals = {
	'A': 1,
	'B': 2,
	'C': 3
}

outcome_pts = {
	'X': 0,
	'Y': 3,
	'Z': 6
}


#input = open('test-input-day2.txt', 'r')
input = open('input-day-2.txt', 'r')
rounds = input.read().split('\n')
#print(rounds)
total_pts = 0

for pair in rounds:
	moves = tuple(pair.split())
	try:
		outcome = moves[1]
	except IndexError:
		print(moves)
		break
	opp_move = moves[0]
	round_pts = 0
	if outcome == 'X': #lose
		round_pts += 0
		move = p_loses[opp_move]
		round_pts += point_vals[move]
		#print(move)
	elif outcome == 'Y': #tie
		round_pts += 3
		move = opp_move
		round_pts += point_vals[move]
	elif outcome == 'Z': #win
		round_pts += 6
		move = p_wins[opp_move]
		round_pts += point_vals[move]
	total_pts += round_pts

print(total_pts)