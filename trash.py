def down(a,b):
    transfer = 0
    while(a % b != 0):
        if b == 0: 
            return float("inf")
        a += 1
        b -= 1
        transfer += 1

    return transfer
    
def up(a,b):
    transfer = 0
    while(a % b != 0):
        a -= 1
        b += 1
        transfer += 1

    if a == 0: 
        return float("inf")
    
    return transfer

def solve(a,b):
    res1=up(a,b)
    res2=down(a,b)

    return min(res1, res2)

t = int(input())

for _ in range(t):
    a, b = [int(el) for el in input().strip().split(" ")]
    print(solve(a,b))
