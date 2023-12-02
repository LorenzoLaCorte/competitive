def pal_primes(target, dp):
    cnt_odd = 0
    cnt_even = 0
    i = 0
    while(cnt_odd + cnt_even < target and i < target):
        i += 1
        y = True
        if(str(i) == str(i)[::-1]):
            if(i>2):
                for a in range(2,i):
                    if(i%a==0):
                        y = False
                        break
                if y:
                    dp[i] = (cnt_even, cnt_odd)
                    if i % 2 == 0:
                        cnt_even += 1
                    else:
                        cnt_odd += 1
                    

dp = [None] * 10**5
t = 2 # int(input())

n_inputs = []
for x in range(t):
    n_inputs.append(1000-x*100) # int(input()))
    
n_inputs.sort(reverse=True)

results = []

for n in n_inputs:
    print(n)
    found = 0
    i = 0
    
    n_even, n_odd = 0, 0

    while(found < n and i < 10**5):
        i += 1
        
        if not dp[n]:
            pal_primes(n, dp)
        

    results.append(f"{n_even} {n_odd}")


results.reverse()
for res in results:
    print(res)