import string
st = input()
num = int(input())
temp_upper = string.ascii_uppercase
temp_lower = string.ascii_lowercase
ans = []
for i in range(len(st)):
    if st[i] in temp_upper:
        temp2 = temp_upper[(temp_upper.index(st[i]) + num) % 26]
        ans.append(temp2)
        print(st[i],temp2,sep=" ")
    elif st[i] in temp_lower:
        temp2 = temp_lower[(temp_lower.index(st[i]) + num) % 26]
        ans.append(temp2)
        print(st[i],temp2,sep=" ")
print("".join(ans))