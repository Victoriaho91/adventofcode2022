from collections import defaultdict
import string 

f= open("input.txt", 'r').read().strip().split('\n')
crates_input = f[:8]
supply_stack = defaultdict(lambda:[])
letters=string.ascii_letters.upper()

for i in range(len(crates_input)):
    stackNum = 1
    #1,5,9,13,17, starting i=1, every i+4 index  
    for j in range(1,len(crates_input[i]),4):
        crate = crates_input[i][j]
        if crate in letters:
            supply_stack[stackNum].append(crate)
        stackNum += 1
directions = f[10:]

print(supply_stack)
def move(arr):
    num_of_crates, from_stack, to_stack=[int(x) for x in list(filter(lambda el: el.isdigit(),arr.split()))]
    return (num_of_crates, from_stack, to_stack)


for direction in directions:
    (num_of_crates, from_stack, to_stack) = move(direction)
    
    for i in range(0,num_of_crates):
        supply_stack[to_stack].insert(i,supply_stack[from_stack].pop(0))

keys = list(supply_stack.keys())
keys.sort()

result = ''.join([supply_stack[key][0] for key in keys])

print(result)
    
