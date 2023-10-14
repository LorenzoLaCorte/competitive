def solve(idx):
    acc = 0
    digits = 0
    base = end = 0

    while acc < idx:
        acc += 9 * 10**digits * (digits+1)
        base = 1 + end
        end = acc
        
        digits += 1

    x = str(((idx-base) // digits) + 10**(digits-1))
    pos = (idx - base) % digits

    # print(f"idx: {idx}")
    # print(f"base: {base}, end: {end}")
    # print(f"digits: {digits}")

    res = x[pos] 
    # print(f"x={x}, pos={pos}, res={res}")
    print(res)


q = int(input())

for _ in range(q):
    k = int(input())
    solve(k)