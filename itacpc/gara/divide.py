from collections import defaultdict
import math

def inp():
    return(int(input()))

def compu(num):
    acc = 0
    far = num
    inc = 1

    while far > 0:
        acc += far
        far = far // (2**inc)
        inc += 1
    
    return acc

def factors(n):
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                yield i
                break

n = inp()
hmap = defaultdict(int)
for factor in factors(n):
    hmap[factor] += 1

print(hmap)
res = 1
for k,v in hmap.items():
    res *= compu(v)

print(res)