from collections import defaultdict
import pdb 
def toInt(calorie):
    list = [x for x in calorie]
    cal = int(''.join(list[:len(list)-1]))
    return cal

lines=None
with open('input.txt') as f:
    lines = f.readlines()

def def_value():
    return []

elf_count = 0
#hashmap to store {elfnum: [calories]}
elfmap= defaultdict(def_value)
for cal in lines:
    if cal != '\n':
        calorie = toInt(cal)
        elfmap[elf_count].append(calorie)
    else:
        elf_count+=1

#sum up all calories for each elf {elfcount: sum}

for key, val in elfmap.items():
    elfmap[key] = sum(val)

def answer(elfmap):
    return max(elfmap.values())

def topthreecals(elfmap):
    cals = list(elfmap.values())
    cals.sort(reverse=True)
    return sum(cals[0:3])

print(topthreecals(elfmap))