# Vowel Repetition Problem
# Given a string s print the most frequent vowel that is present in the string as a output.
# Input Format:
# A single line containing the string s.
# The input will be read from the STDIN by the candidate
# Output Format:
# Print a single character which represents the most frequent vowel in the given string.
# Example:
# Input:
# helloworld
# Output:
# O

# 1st app
s = input().lower()
v='aeiou'
mx=0
vowel=''
for i in v:
    if s.count(i)>mx:
        mx=s.count(i)
        vowel=i
print(vowel)

# 2nd app
s = input().lower()
v = {'a': 0,'e': 0,'i': 0,'o': 0,'u': 0}
for i in s:
    if i in v:
        v[i] += 1
for i in v:
    if v[i]==max(v.values()):
        print(i)
        break