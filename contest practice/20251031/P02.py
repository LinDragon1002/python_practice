import string
inputs = input()
temp = string.ascii_lowercase+string.ascii_uppercase
ans = 0
for i in range(len(inputs)):
    ans_str = ""
    ans_str += inputs[i]
    for j in range(i+1,len(inputs)):
        if temp.index(inputs[j-1]) < temp.index(inputs[j]):
            ans_str += inputs[j]
        else:
            break
    ans = max(ans,len(ans_str))
print(ans)