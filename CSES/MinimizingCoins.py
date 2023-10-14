import sys

sys.setrecursionlimit(10000000)

def solve(n, coins, results):
    if n == 0:
        return 0

    coin_needed = 0
    coin_costs = []

    for coin in coins:
        if coin > n: 
            continue

        if results[n-coin]:
            coin_needed = results[n-coin] 
        else:
            coin_needed = solve(n - coin, coins, results)
            results[n-coin] = coin_needed

        if coin_needed != -1:
            coin_costs.append(coin_needed) 

    if len(coin_costs) == 0: 
        return -1
    
    coin_cost = 1 + min(coin_costs)
    return coin_cost

# 4 37
# 2 3 28 33

_, n = [int(el) for el in input().strip().split(" ")]
coins = [int(el) for el in input().strip().split(" ")]
results = [None]*n
print(solve(n, coins, results))