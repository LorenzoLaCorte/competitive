def insr(): # strings as list of char
    s = input()
    return(list(s[:len(s)]))

s = insr()
ch = chr(sum([ord(c) for c in s])//len(s))
print(ch)