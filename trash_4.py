def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
  

def solve(health):
    if health == 1:
        return 1

    # Check if it's impossible to kill the monster
    if health % 2 == 0 or is_prime(health):
        return -1
        
    moves = 0
    power = 1
    
    special = False
    
    while(health > 0):
        moves += 1

        if (is_prime(health-power)) and not special:
            health -= health-power
            special = True
        else:
            health -= power
            power *= 2

    if health == 0:
        return moves
    else:
        return -1
    

t = int(input())

for _ in range(t):
    health = 10 # int(input())
    print(solve(health))
