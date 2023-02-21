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


t = inp()
acc = 0
m = 0

for _ in range(t):
    n = inp()
    acc += n
    m = min(acc, m)

print(abs(m))