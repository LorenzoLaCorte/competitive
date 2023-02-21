def inlt():
    return(list(map(int,input().split())))
def inp():
    return(int(input()))

# n: number of ingredients          2
# x: number of portions produced    4
# y: number of portions needed      10
n, x, y = inlt()

for _ in range(n):
    # amounts of each ingredient needed
    a = inp() # 8 12
    print(a * y // x)


