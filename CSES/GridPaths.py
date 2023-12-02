MOD = (10**9 + 7)

n = int(input())

# dp is filled with zeros or -1
# if zeros it means that it has to be filled
# if -1 it means that is a trap
dp = []

for i in range(n):
    row = []
    line = str(input().strip())
    for j, el in enumerate(line):
        if el == ".": 
            if i == 0 and j == 0:
                row.append(0)
            elif (i == 1 and j == 0) or (i == 0 and j == 1):
                row.append(1)
            elif i == 0:
                tmp = 1 if row[j-1] == 1 else 0 
                row.append(tmp)
            elif j == 0:
                tmp = 1 if dp[i-1][0] == 1 else 0
                row.append(tmp)
            else:
                row.append(0)
        else: 
            row.append(-1)
    dp.append(row)

if dp[0][0] == -1 or dp[n-1][n-1] == -1:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(1,n):
        for j in range(1,n):
            if dp[i][j] != -1:
                tmp = 0
                if dp[i-1][j] != -1:
                    tmp = (tmp + dp[i-1][j]) % MOD 
                if dp[i][j-1] != -1:
                    tmp = (tmp + dp[i][j-1]) % MOD 
                dp[i][j] = tmp

    res = dp[n-1][n-1] if dp[n-1][n-1] != -1 else 0
    print(res)