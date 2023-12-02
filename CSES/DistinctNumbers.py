n = int(input())
nums = [int(el) for el in input().strip().split(" ")]

nums.sort()

res = 1
curr = nums[0]

for num in nums[1:]:
    if num != curr:
        res += 1
        curr = num

print(res)