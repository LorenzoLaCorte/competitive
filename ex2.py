from collections import defaultdict

def solve(n, a, col_a, b, col_b):
    col_to_el = defaultdict(lambda: [[], []])

    for i in range(n):

        col_to_el[col_a[i]][0].append(a[i])
        col_to_el[col_b[i]][1].append(b[i])
        
    
    print(col_to_el)
    
    for colour, arrays in col_to_el.items():
        arr_a = arrays[0]
        arr_b = arrays[1]
        
        for i in range(len(arr_a)-1):
            if arr_a[i] <= arr_a[i+1]:
                continue
            else:
                # try swapping
                min_el_b = min(arr_b)
                idx_el_b = arr_b.index(min_el_b)
                arr_a[idx_el_b], arr_b[idx_el_b] = arr_b[idx_el_b], arr_a[idx_el_b]
                
                if arr_a[i] > arr_a[i+1]:
                    return "No"

    print(col_to_el)
        


t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(el) for el in input().strip().split(" ")]
    col_a = [int(el) for el in input().strip().split(" ")]
    b = [int(el) for el in input().strip().split(" ")]
    col_b = [int(el) for el in input().strip().split(" ")]
    print(solve(n, a, col_a, b, col_b))