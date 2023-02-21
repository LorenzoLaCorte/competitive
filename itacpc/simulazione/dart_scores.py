# sections from 1 to 20
# when player its i scores
    # i in the normal area
    # 2i in the double area
    # 3i in the triple area
# three throws

# given a target score  1 <= n <= 180
# output at most three throw scores
    # such that their sum is equal to target

import sys
input = sys.stdin.readline

def inp():
    return(int(input()))

hm_type = {1: "single", 2: "double", 3: "triple"}

def solve(n):
    
    shots = 0
    out = ""

    while n > 0:
        shots += 1
        if shots > 3: 
            print("impossible")
            break


        # compute what shot to do
        if n <= 20:
            type = 1
            shot = n
        elif n <= 40:
            type = 2
            shot = n//2
        else:
            type = 3
            shot = min(20, n//3)

        out += (hm_type[type] + " " + str(shot) + "\n")
        n -= shot*type

    if shots <= 3: 
        print(out[:-1])

def solve2(n):
    shots = 0
    out = ""

    while n > 0:
        shots += 1
        if shots > 3: 
            print("impossible")
            break

        # compute what shot to do
        if n <= 20:
            type = 1
            shot = n
        elif n <= 40 and n%2==0:
            type = 2
            shot = n//2
        else:
            type = 3
            shot = min(20, n//3)

        out += (hm_type[type] + " " + str(shot) + "\n")
        n -= shot*type

    if shots <= 3: 
        print(out[:-1])


n = inp()
solve2(n)


