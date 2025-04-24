st = input()
for i in range(1,len(st)-1):
    if st[i-1] > st[i] and st[i] < st[i+1]:
        print("1")
        break
else:
    print("0")