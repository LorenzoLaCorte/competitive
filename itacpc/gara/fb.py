from collections import defaultdict

def inlt():
    return(list(map(int,input().split())))
    
hmap = defaultdict(set)
N, M, K = inlt()

for _ in range(M):
    x, y = inlt()
    
    hmap[x].add(y)
    hmap[y].add(x)

sets = list(hmap.values())

for i, s1 in enumerate(sets):
    for s2 in sets[i+1:]:
        if len(s1 & s2) >= K:
            print("YES")
            exit(0)

print("NO")