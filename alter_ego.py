import random

def solve(n, a):
    if sum(a) % 2 != 0:
        return [-1]
    b = [0] * len(a)
    idx_start2 = len(a)//2
    
    while not all((a[i] + a[i + 1]) % 2 == 0 for i in range(0, len(a), 2)):
        random.shuffle(a)
            
    # take couples in the array
    for i in range(0, len(a), 2):
        mid = (a[i] + a[i+1]) // 2
        variance = abs(a[i] - mid)
        
        b[idx_start2 - i//2 - 1] = mid
        b[len(a) - i//2 - 1] = variance
    
    return b

t = int(input())

for _ in range(t):
    n = int(input())
    elements = [int(el) for el in input().strip().split(" ")]
    print(*solve(n, elements))