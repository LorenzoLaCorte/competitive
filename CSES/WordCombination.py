# You are given a string of length n and a dictionary containing k words. 
# In how many ways can you create the string using the words?


def solve(mystr, words):
    trie = [[0]*26]
    stop_trie = [[0]*26]

    for word in words:
        i = 0
        for idx,c in enumerate(word):
            # print(f"\nProcessing char {idx} of {word}")
            if trie[i][ord(c)-ord('a')] == 0:
                new_list = [0]*26
                trie.append(new_list)

                stop_trie.append(new_list.copy())
                if idx == len(word)-1: 
                    stop_trie[i][ord(c)-ord('a')] = 1
                    # print(f"Inserting Placeholder (1) in trie[{i}][{ord(c)-ord('a')}] to identify end of {word}")

                new_idx = len(trie) - 1
                trie[i][ord(c)-ord('a')] = new_idx
                # print(f"Inserting {(new_idx)} in trie[{i}][{ord(c)-ord('a')}] to identify {c}")
                i = new_idx
                # print(f"i equals to {len(trie)-1}")
            else:
                # print(f"i equals to {trie[trie[i][ord(c)-ord('a')]]}")
                i = trie[i][ord(c)-ord('a')]
    
    res = 1
    ways = 0
    i = 0
    idx = 0

    while idx <= len(mystr):
        if idx == len(mystr): 
            res *= ways
            break
        c = mystr[idx]
        if i == 0 and trie[i][ord(c)-ord('a')] == 0:
            break
        elif trie[i][ord(c)-ord('a')] != 0:
            if stop_trie[i][ord(c)-ord('a')] == 1:
                ways += 1
            i = trie[i][ord(c)-ord('a')]
            idx += 1
        else:
            res *= ways
            i = 0
            ways = 0
                        
    return (res % (10**9 + 7))


# print(solve("ababc", ["ab", "abab", "c", "cb"]))

words = []
mystr = str(input())
t = int(input())

for _ in range(t):
    words.append(str(input()))
print(solve(mystr, words))
