def inlt():
    return(list(map(int,input().split())))
def inp():
    return(int(input()))

t = inp() # 10^4

for _ in range(t):
    n = inp() #  the number of members of the group excluding Beppa, max 10^5

    # they are all different
    ids1 = inlt()
    ids2 = inlt() 

    p1 = p2 = n-1 # pointers to lists

    while True:
        while ids1[p1] != ids2[p2] and p1 != 0:
            p1 -= 1

        if p1 == 0: 
            if ids1[p1] == ids2[p2]:
                p2 -= 1
            break

        p2 -= 1

    print(p2+1)