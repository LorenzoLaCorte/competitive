def insr(): # strings as list of char
    s = input()
    return(list(s[:len(s)]))

pwd1 = insr()
pwd2 = insr()

count = 0
for idx, _ in enumerate(pwd1):
    if pwd1[idx] != pwd2[idx]:
        count += 1

print(2**count)