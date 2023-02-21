def solve(n, sequence):
    return -1

t = int(input())

for _ in range(t):
    n = int(input())
    sequence = [int(el) for el in input().strip().split(" ")]
    print(solve(n, sequence))
