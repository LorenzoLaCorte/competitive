def inlt():
    return(list(map(int,input().split())))
def inp():
    return(int(input()))

n = inp()
count = 0
for _ in range(n):
    num = input()    
    if 12 <= len(num) <= 13 and num[:3] == "+39":
        count += 1

print(count)
    


