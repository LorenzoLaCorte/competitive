def solve_4(nums):
    results2 = []
    results4 = []

    # number of op to make product of nums % k
    for num in nums:
        results2.append(2 - num%2 if num%2 != 0 else 0)
        results4.append(4 - num%4 if num%4 != 0 else 0)
    
    # sum first and second min
    first = min(results2)
    results2.remove(first)
    second = min(results2)

    return min(first+second,min(results4))


def solve(nums,k):
    if k == 4: 
        return solve_4(nums)   
     
    results = []
    for num in nums:
        results.append(k - num%k if num%k != 0 else 0)
    
    return min(results)

# print(solve([9, 5, 1, 5, 9, 5, 1],4))
# print(solve([3, 5, 3],4))
# print(solve([6, 1, 5],4))

t = int(input())

for _ in range(t):
    _, k = [int(el) for el in input().strip().split(" ")]
    nums = [int(el) for el in input().strip().split(" ")]
    print(solve(nums,k))

