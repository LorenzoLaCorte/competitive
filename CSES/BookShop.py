def solve(n, budget, prices, pages, dp):
    for j in range(n):
        for i in range(budget-prices[j], -1, -1):
            cost = i + prices[j]
            if cost <= budget:
                dp[cost] = max(dp[cost], dp[i] + pages[j])
    return dp[budget]


n, budget = [int(el) for el in input().strip().split(" ")]

prices = [int(el) for el in input().strip().split(" ")]
pages = [int(el) for el in input().strip().split(" ")]

dp = [0] * (budget+1)

print(solve(n, budget, prices, pages, dp))