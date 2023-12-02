maxN = 100
maxX = 10**6
MOD = (10**9 + 7)

def solve(coins, sum, dp):
    # go incrementally
    for i in range(0, sum):
        if dp[i] != 0:
            for coin in coins:
                tmp_sum = i+coin
                if tmp_sum <= sum:
                    dp[tmp_sum] = (dp[tmp_sum] + dp[i]) % MOD
      
    return dp[sum]


_, sum = [int(el) for el in input().strip().split(" ")]
coins = [int(el) for el in input().strip().split(" ")]
dp = [1] + [0]*(sum)

print(solve(coins, sum, dp))