txt = 'ABABACDEABABABCABCABCABDAA'
pat = 'ABCAB'
for i in range(len(txt) - len(pat)+ 1):
    match = True
    for j in range(len(pat)):
        if txt[i + j] != pat[j]:
            match = False
            break
    if match:
        print("Pattern found at index:", i)

