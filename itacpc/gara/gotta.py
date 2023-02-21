def inp():
    return(int(input()))

n = inp()
pokemons = set()
res = 0
for i in range(n):
    poke = input()    
    pokemons.add(poke)

print(len(pokemons)+1)