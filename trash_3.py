

def solve(a,b):
    if a % b == 0:
        return 0
    elif a >= b:
        return b - (a % b)
    else:
        return b - (b % a)

t = int(input())

for _ in range(t):
    a, b = [int(el) for el in input().strip().split(" ")]
    print(solve(a,b))
