words = ["a","b"]
temp = ["qwertyuiop","asdfghjkl","zxcvbnm"]
ans = []
temp_num = [0,0,0]
for i in words:
    for j in i:
        if j.lower() in temp[0]:
            temp_num[0] += 1
        elif j.lower() in temp[1]:
            temp_num[1] += 1
        else:
            temp_num[2] += 1
        if temp_num.count(0) < 2:
            temp_num = [0,0,0]
            break
    else:
        ans.append(i)
print(ans)
'''
["Alaska","Dad"]
'''