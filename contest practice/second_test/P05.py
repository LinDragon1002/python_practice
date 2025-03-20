st = [i for i in input()]
temp1 = ""
temp2 = ""
for i in range(len(st)):
    if st[i] == "=":
        for j in range(i+1,len(st)):
            temp2+=st[j]
        break
    else:
        temp1+=st[i]
if eval(temp1) == eval(temp2):
    print(1)
else:
    print(0)