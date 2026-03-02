ransomNote = "aa"
magazine = "aab"
from typing import Counter
temp1 = Counter(magazine)

for i in ransomNote:
    if i in magazine and temp1[i] > 0:
        temp1[i] -= 1
    else:
        print(False)
        break
else:
    print(True)


for i in set(ransomNote):
    if magazine.count(i) < ransomNote.count(i):
        # return False
        print()
# return True
print()