input= open("input.txt", 'r').read()

''''
4 unique letters in a row
if p2 letter not in seen, add to obj (letter: last seen idx) 
if p2 is in seen, move p1 to lastseen idx+1 and update seen[letter] to p2
    if any idx in seenObj is less than p1, remove it 
p2++ 


after adding to seen if p2 -p1 = 3, return p2+1 
seen {m:0, g:3, t:2, d:5 }
m g t g d d t f d t f f z v z nvnrncrrbqqhlhhffzqqzpqqt
          1 2
'''
def part1 (input):
    p1, p2 = 0,0
    seen={}
    while(p2<len(input)):
        if input[p2] not in seen:
            seen[input[p2]] = p2
            if p2-p1 ==3:
                return p2+1 
        else:
            p1 = seen[input[p2]] +1 
            seen[input[p2]] = p2
            for key, val in list(seen.items()):
                if val<p1:
                    del seen[key]

        p2+=1

def part2 (input):
    p1, p2 = 0,0
    seen={}
    while(p2<len(input)):
        if input[p2] not in seen:
            seen[input[p2]] = p2
            if p2-p1 ==13:
                return p2+1 
        else:
            p1 = seen[input[p2]] +1 
            seen[input[p2]] = p2
            for key, val in list(seen.items()):
                if val<p1:
                    del seen[key]

        p2+=1
print(part1(input))
print(part2(input))