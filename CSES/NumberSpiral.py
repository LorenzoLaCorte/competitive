# A number spiral is an infinite grid whose upper-left square has number 1. Here are the first five layers of the spiral:
# Your task is to find out the number in row y and column x

# Input: The first input line contains an integer t : the number of tests.
# After this, there are t lines, each containing integers y and x

# Output: for each test, print the number in row y and column x


def solve(y,x):
    invert = False
    if y > x:
        x, y = y, x
        invert = True

    pivot = x**2

    if (x % 2 != 0 and not invert) or (x % 2 == 0 and invert):
        res = pivot - y + 1
    else:
        res = pivot - 2*x + y + 1

    print(res)


t = int(input())

for _ in range(t):
    y, x = [int(el) for el in input().strip().split(" ")]
    solve(y,x)