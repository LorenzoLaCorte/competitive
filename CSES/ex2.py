from collections import defaultdict

def solve(s,k):
    letters = defaultdict(int)
    for c in s:
        letters[c] += 1

    for _, occ in letters.items():
        if occ % 2 != 0:
            k -= 1
            if k < -1: 
                print("NO")
                return
            
    print("YES")

# solve("zwaafa", 2)
# solve("a", 0)
# solve("ab", 0)

t = int(input())

for _ in range(t):
    _, k = [int(el) for el in input().strip().split(" ")]
    s = str(input())
    solve(s,k)

