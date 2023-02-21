from collections import defaultdict


def inlt():
    return(list(map(int,input().split())))

def solve(hmap):

#    sets = []

#   for k, v in hmap.items():
#        sets.append((v))

    s_count_ds = []
    for s in range(37):
        count = 0
        for d in range(37):
            if s in hmap:
                if d in hmap[s]:
                    count += 1
        s_count_ds.append(count)
    
    # print(s_count_ds)
    maxm = 0
    for k in range(1, 37):
        count = len([i for i in s_count_ds if i >= k])
        if count >= k:
            maxm = k
    return maxm


n = int(input()) # num of scenarios
hmap = {}

for _ in range(n):
    m = int(input()) # num of vases
    
    if m==0: 
        print(0)
        continue

    hmap = {}

    for i in range(m):
        s, d = inlt()
        if s not in hmap:
            hmap[s] = set()
        hmap[s].add(d)

    # print(hmap)
    print(str(solve(hmap)))
