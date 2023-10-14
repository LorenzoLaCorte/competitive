start_word = input()
t = int(input())

w_list = [start_word]
dict_l = []

for _ in range(t):
    dict_l.append(input())

for i in range(0, len(start_word)):
    for word in w_list:
        j = 0
        
        # move j till _ chars
        while (j<len(word) and word[j] == "_"):
            j+=1

        if word[j:i+1] in dict_l:
            w_list.append("_" * (i+1) + word[i+1:] )

print(w_list.count("_"*len(start_word)))