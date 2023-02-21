def inlt():
    return(list(map(int,input().split())))
def inp():
    return(int(input()))
    
def pal_up_to_n(n):
    if n < 1:
        return 0
    if n % 2 == 0:
        return 2*10**(n//2) - 2
    else:
        return 11*10**(n//2) - 2

def below(n):
    if n < 1:
        return 0
    if n < 10:
        return n 

    dec = str(n)
    digits = len(dec)
    count = pal_up_to_n(digits-1) + 1
    half_length = (digits-1) // 2
    front_part = dec[0:half_length + 1]
    count += int(front_part) - 10**half_length
    i, j = half_length, half_length+1
    if digits % 2 == 1:
        i -= 1
    while i >= 0 and dec[i] == dec[j]:
        i -= 1
        j += 1
    if i >= 0 and dec[i] < dec[j]:
        count += 1
    return count

def count_pal(start, end):
    return below(end+1) - below(start)

n = inp()
for _ in range(n):
    x, y = inlt()
    print(count_pal(x, y))