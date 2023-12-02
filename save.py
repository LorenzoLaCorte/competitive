def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
  

def solve(health):
    power_of_two = 0
    possible_res = []
    
    while(2**power_of_two < health):
        health -= 2**power_of_two
        possible_res.append(health)
    
    

t = int(input())

for _ in range(t):
    health = int(input())
    print(solve(health))