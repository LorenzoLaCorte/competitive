def inp():
    return(int(input()))

def inlt():
    return(list(map(int,input().split())))

def myOp(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a != b:
        raise ValueError()
    return a

def merge(row1, row2):
    return [myOp(a,b) for a,b in zip(row1, row2)]
    
rows, infls = inlt()
A = []
coherent = {}
gains = []

for i in range(rows):
    color, start, end = inlt()
    curr_row = [color if start <= idx <= end else None for idx in range(infls)]

    coherent[i] = []
    for j, row in enumerate(A):
        if i==j: continue
        try:
            merge(curr_row, row)
            coherent[i].append(j)
        except:
            pass

    A.append(curr_row)

print(A)

'''
    0 0 N N N  | 2
    0 0 0 N N  | 3
    1 N N N N  | 1

    0 | 2
    0,1 | 5
'''