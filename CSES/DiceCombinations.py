from __future__ import annotations

def combinations(n, results) -> int:
    # if we know it return it immediately
    if results[n]:
        return results[n]
    
    acc = 0
    for i in range(n-6, n):
        if not results[i]:
            # compute from results[i] to results[i+6] 
            j = 6
            while j != i+6:
                results[j+1] = sum(results[j-5:j+1]) % (10**9+7) 
                j += 1
        acc += results[i]

    results[n] = acc % (10**9+7) 
    return results[n]

if __name__ == "__main__":
    n = (int(input()))
    results = [1,1,2,4,8,16,32]+[None]*(n)
    print(combinations(n, results))