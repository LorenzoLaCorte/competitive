INF = float('inf')
 
n = int(input())
# keep all base cases (one digit)
dp = [0] + ([1] * 9) + ([INF] * n)

for i in range(0,n+1):
    digits = str(i)

    # sum of the minimum required step among those obtained by subtracting digit1, digit2, ..
    for digit in digits:
        dp[i] = min(dp[i], dp[i-int(digit)]+1)
    
print(dp[n])