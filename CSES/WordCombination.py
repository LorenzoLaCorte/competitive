# You are given a string of length n and a dictionary containing k words. 
# In how many ways can you create the string using the words?


def solve(mystr, words):
    res = 0

    # Create the Trie
    trie = [[0]*26]

    for word in words:
        i = 0
        for idx,c in enumerate(word):
            print(f"\nProcessing char {idx} of {word}")
            if trie[i][ord(c)-ord('a')] == 0:
                new_list = [0]*26
                trie.append(new_list)
                trie[i][ord(c)-ord('a')] = len(trie)-1
                print(f"Inserting {(len(trie)-1)} in trie[{i}][{ord(c)-ord('a')}] to identify {c}")
                i = len(trie) - 1
                # print(f"i equals to {len(trie)-1}")
            else:
                # print(f"i equals to {trie[trie[i][ord(c)-ord('a')]]}")
                i = trie[i][ord(c)-ord('a')]
    

    # Print the number of ways modulo (10**9 + 7)
    # print(res % 10**9 + 7)

solve("ababc", ["ab", "abab", "c", "cb"])