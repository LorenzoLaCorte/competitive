NUMS = [1,2,3,4,5,6,7,8,9,0]

def solve(x):
    res = 0
    pos = 0
    for num in str(x):
        
        num = int(num)
        target = NUMS.index(num) 
        res += abs(target-pos) + 1

        pos = target
    
    return res

# print(solve("8361"))
# print(solve("0294"))

t = int(input())

for _ in range(t):
    x = input()
    print(solve(x))

