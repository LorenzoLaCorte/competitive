def isPalindrome(n):
    return str(n) == str(n)[::-1]

def isPrime(n):
    if n < 2: 
         return False;
    if n % 2 == 0:             
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

def process(n, primes, palindromes, results):
    found = 0
    i = 0
    
    n_even, n_odd = 0, 0

    while(found < n and i < 10**5):
        i += 1
        
        if primes[i] == -1:
            primes[i] = isPrime(i)
            palindromes[i] = isPalindrome(i)
            max_i = i
        
        if primes[i] and palindromes[i]:
            
            if len(str(i)) % 2 == 0: 
                n_even += 1
            else:
                n_odd += 1
                
            found += 1
        
    results.append(f"{n_even} {n_odd}")

t = int(input())

primes = [0] + [-1] * (10**5)
palindromes = [0] + [-1] * (10**5)
n_inputs = []
for _ in range(t):
    n_inputs.append(int(input()))
    
n_inputs.sort(reverse=True)
print(n_inputs)

results = []

for n in n_inputs:
    

results.reverse()
for res in results:
    print(res)