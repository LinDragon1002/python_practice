st = [i for i in input()]
num = 0
for i in range(len(st)):
    if st[i] != "(" and st[i] != ")":
        st[i] = "="
    elif st[i] == "(":
        num += 1
    elif st[i] == ")":
        num -= 1
    if num 
    
print(st)