from collections import defaultdict

def solve(n, a, col_a, b, col_b):
    col_to_el = defaultdict(lambda: [[], []])

    for i in range(n):

        col_to_el[col_a[i]][0].append(a[i])
        col_to_el[col_b[i]][1].append(b[i])
    
    
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
    
    len_tot = len(a)
    for i in range(len_tot - 1):
        if a[i] <= a[i+1]:
            continue
        else:
            # try to swap with the min number of the el in b with the corresponding colour
            matching_idxs = [j for j, e in enumerate(col_b) if e == col_a[i]]
            # take the minimum among those
            matching_min = min([b[idx] for idx in matching_idxs])
            
            if matching_min > a[i+1]:
                return "No"
            matching_idx = b.index(matching_min)
            # and swap
            a[matching_idx], b[matching_idx] = b[matching_idx], a[matching_idx]
    
    return "Yes"
        


t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(el) for el in input().strip().split(" ")]
    col_a = [int(el) for el in input().strip().split(" ")]
    b = [int(el) for el in input().strip().split(" ")]
    col_b = [int(el) for el in input().strip().split(" ")]
    print(solve(n, a, col_a, b, col_b))
