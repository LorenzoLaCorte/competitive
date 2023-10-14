'''
6
14
100 200 300 400 500 600 700 800 900 1000 1100 1200 1300 1400
12
100 200 300 400 600 700 800 900 1100 1200 1300 1400
13
100 200 300 400 500 600 700 800 900 1100 1200 1300 1400
13
101 189 272 356 463 563 659 739 979 1071 1170 1274 1358
1
42
5
0 1 2 3 4

Output
Copy

NO
YES
NO
YES
YES
YES
'''

def inlt():
    return(list(map(int,input().split())))
def inp():
    return(int(input()))

t = inp()

for _ in range(t):
    n = inp()
    tmp = inlt()
    mex = [0]+tmp+[1440]

    count = 0
    for i in range(0, len(mex)-1):
        s = mex[i]
        e = mex[i+1]

        count += (e-s) // 120

    if count >= 2: print("YES")
    else: print("NO")