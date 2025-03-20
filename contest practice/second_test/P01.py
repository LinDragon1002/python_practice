st = [int(i) for i in input().split()]
num1 = st[1] - st[0]
num2 = st[1] // st[0]
ans = [0,0]
for i in range(len(st)-1):
    if st[i+1] - st[i] == num1:
        ans[0] += 1
for i in range(len(st)-1):
    if st[i+1] // st[i] == num2:
        ans[1] += 1
if ans[0] > 1 and ans[1] == 0:
    print("A")
    print(num1)
elif ans[1] > 1 and ans[0] == 0:
    print("G")
    print(num2)
