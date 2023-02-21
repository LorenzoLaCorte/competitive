from collections import defaultdict
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))

def inlt():
    return(list(map(int,input().split())))

def insr(): # strings as list of char
    s = input()
    return(list(s[:len(s) - 1]))

def invr(): # taking space separated integer variable inputs
    return(map(int,input().split()))

def solve(sequence, n):

    acc = 0
    for idx, el in enumerate(sequence):
        acc += el
        sequence[idx] = acc

    # print(sequence)

    maxima = defaultdict(int) # mapping first el of the sequence with his maxiumum number if steps btw multiples
    
    for i, el in enumerate(sequence):
        if sequence[-1] % el != 0: continue
        factor = 2
        idx = i # idx of last multiple
        maxima[el] = i+1
        # search for multiples of increasing factor of el
        for j in range(i+1, len(sequence)):
            cmp = sequence[j]
        
            if j == len(sequence)-1 and cmp != el * factor:
                maxima[el] = n
                break

            if cmp == el * factor:
                maxima[el] = max(maxima[el], (j - idx))
                factor += 1
                idx = j  

            elif cmp > el * factor:
                maxima[el] = n
                break

    return min(maxima.values(), default=1) 

t = inp()

for _ in range(t):
    n = inp()
    sequence = inlt()
    print(solve(sequence, n))

