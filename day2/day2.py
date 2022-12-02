'''
The score for a single round is the score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the 
outcome of the round (0 if you lost, 3 if the round was a draw, and 
6 if you won).
X for Rock, Y for Paper, and Z for Scissors. 

part 2:
X,Y,Z : lose, draw, win
'''

f= open("input.txt", 'r').read().split('\n')
roundpoints = 0
roundresult = 0

add_game_points ={
'X': 1,
'Y': 2,
'Z': 3
}

rules={
    'A': {'X':3, 'Y':6, 'Z':0},
    'B': {'X':0, 'Y':3, 'Z':6},
    'C': {'X':6, 'Y':0, 'Z':3}
}

for i in f:
    game = i.split(' ')
    opponent, self = game
    roundpoints += add_game_points[self]
    roundresult += rules[opponent][self]

total = roundpoints + roundresult

print(f'Answer to part 1: {total}')


roundpoints = 0
roundresult = 0

part2_rules ={
    'A': {'X':3, 'Y':1, 'Z':2},
    'B': {'X':1, 'Y':2, 'Z':3},
    'C': {'X':2, 'Y':3, 'Z':1}
}

add_result_points ={
    'X': 0,
    'Y': 3,
    'Z': 6
}

for i in f:
    game = i.split(' ')
    opponent, result = game
    roundpoints += part2_rules[opponent][result]
    roundresult += add_result_points[result]
total = roundpoints + roundresult
print(f'Answer to part 2: {total}')