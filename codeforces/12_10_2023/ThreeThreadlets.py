# In one operation, Decim chooses any threadlet
# cuts it into two threadlets, 
# whose lengths are positive integers 
# and their sum is equal to the length of the threadlet being cut.

# Decim can perform at most three operations. 
# He is allowed to cut the threadlets obtained from previous cuts. 
# Will he be able to make all the threadlets of equal length?

def are_all_elements_equal(lst):
    if not lst:
        return True
    
    first_element = lst[0]
    return all(element == first_element for element in lst)

def find_max(input_list):
    max = input_list[0]
    index = 0
    for i in range(1,len(input_list)):
        if input_list[i] > max:
            max = input_list[i]
            index = i
    return max, index

def solve(t):
    if t[0] == t[1] == t[2]:
        return "YES"
    
    goal = min(t)
    big, big_idx = find_max(t)
    steps = 0

    factor = 1

    if goal == 1:
        factor = 2
    else:
        tmp = goal
        while (tmp < big):
            tmp = goal**factor
            factor += 1

    splits = [t]

    while steps < 4:
        steps += 1
        new_splits = []
        for split in splits:
            if are_all_elements_equal(split): 
                return "YES"
            if steps <= 3:
                big, big_idx = find_max(split)
                del split[big_idx]
                for i in range(1, factor):
                    new_splits.append(split + [big-(goal**i), (goal**i)])
        splits = new_splits        
    return "NO"


# print(solve([9,3,6]))
t = int(input())

for _ in range(t):
    n, m, p = [int(el) for el in input().strip().split(" ")]
    print(solve([n, m, p]))
