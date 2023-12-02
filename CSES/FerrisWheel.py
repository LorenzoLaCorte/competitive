n, x = [int(el) for el in input().strip().split(" ")]
weights = [int(el) for el in input().strip().split(" ")]

weights.sort()

count = 0
i, j = 0, n-1

while i <= j and i < n and j >= 0:
    if i != j and weights[i] + weights[j] <= x:
        j -= 1

    i += 1    
    count += 1

print(count)