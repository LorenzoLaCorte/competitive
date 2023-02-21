def inlt():
    return(list(map(int,input().split())))
def inp():
    return(int(input()))

args = inlt()

grade = args[0] # is btw 1 and 6
acc = args[grade+1]

# compute p_n
for i in range(grade, 0, -1):
    acc += args[i] + i**i

p_n = acc
print(args[grade+1])
acc = args[grade+1]

for i in range(grade, 0, -1):
    C_i = p_n - acc
    acc += C_i
    print(C_i)

# grade 2
# a_0 = 5
# a_1 = -4
# a_2 = 2

# P(0) = 5
# P(i) = P(i-1) + t_1 + ... + t_n
# P(n) = a_n * n^n + ... + a_0 = P(i-1) + t_1 + ... + t_n

# t_n = P(n) - t_(n-1) - .... - t_0
# t_0 = 5
# t_1 = P(n) - 5

# P(n) = a_n * x^n + ... + a_0 = 
# C_1 = t_1 = t_1 + t_2
# C_2 = 