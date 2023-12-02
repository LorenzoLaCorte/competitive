def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6. 
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True    
  

def solve(health):
    moves = 0
    power = 1
    
    special = False
    
    while(health > 0):
        used_now = False
        moves += 1
        tmp_power = power
        
        if not special:
            while(tmp_power <= health):
                if (is_prime(health-tmp_power)):
                    health -= power
                    special = True
                    used_now = True
                tmp_power *= 2
            
        if used_now:  
            continue
        
        health -= power
        power *= 2

    return -1        
    

t = int(input())

for _ in range(t):
    health = int(input())
    print(solve(health))
