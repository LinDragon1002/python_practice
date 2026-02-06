s = "rat"
t = "cat"
temp1 = set(s)
temp2 = set(t)
if len(temp1) == len(temp2):
    for i in temp1:
        if s.count(i) != t.count(i):
            print(False)
            break
    else:
        print(True)
        
else:
    print(False)