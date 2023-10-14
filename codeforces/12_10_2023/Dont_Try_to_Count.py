def solve(x, s):
    if s in x:
        return 0
    
    count = 0
    while(count < 2 or len(x) <= len(s)):
        count += 1 
        x += x
        if s in x:
            return count
    
    return -1


t = int(input())

for _ in range(t):
    n, m = [int(el) for el in input().strip().split(" ")]
    x = str(input())
    s = str(input())
    # print(f"res is: {solve(x, s)}")
    print(solve(x, s))
