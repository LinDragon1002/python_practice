import string
st = input()
num = int(input())
ans = ''
temp1 = string.ascii_lowercase
temp2 = string.ascii_uppercase
for i in st:
    if i in temp1:
        ans += temp1[(temp1.index(i) + num) % 26]
        print(i,temp1[(temp1.index(i) + num) % 26])
    elif i in temp2:
        ans += temp2[(temp2.index(i) + num) % 26]
        print(i,temp2[(temp2.index(i) + num) % 26])
print(ans)