s = "b"
t = "abc"

if len(s) == 0:
    print(True)
count = 0
for i in t:
    if len(s) <= count:
        break
    if s[count] == i:
        count += 1
if count == len(s):
    print(True)
else:
    print(False)