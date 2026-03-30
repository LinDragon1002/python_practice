s = "eedede"

from collections import Counter
count = 0
temp = Counter(s)
temp_s = s
if s == s[::-1]:
    print(True)
else:
    for i in temp:
        if temp[i] % 2 != 0:
            temp_s = temp_s.replace(i, "")
            if temp_s == temp_s[::-1]:
                print(True)
                break
    else:
        print(False)

# 另解
'''
def valid_palindrome(i,j):
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

i=0
j=len(s)-1
while i<j:
    if s[i]!=s[j]:
        return valid_palindrome(i+1,j) or valid_palindrome(i,j-1)
    i+=1
    j-=1
return True
'''