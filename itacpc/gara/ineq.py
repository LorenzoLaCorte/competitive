from collections import defaultdict


def inlt():
    return(list(map(int,input().split())))
def inp():
    return(int(input()))

n = inp()

hmap = defaultdict(lambda: 'N')

for _ in range(n):
    ineq = input()
    
    if ineq[2] == '>':
        hmap[ineq[0]] = ineq[4]
    
    else:
        hmap[ineq[4]] = ineq[0]

flag = True
tmp = list(hmap.keys()).copy()
for k in tmp:
    curr = hmap[k]
    while curr != 'N':
        if hmap[curr] == k:
            flag = False
            break
        curr = hmap[curr]

if flag: print(":)")
else: print(":(")
