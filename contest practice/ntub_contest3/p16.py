ans = [1,1]
a,b = map(int,input().split())
while True:
    temp = ans.append(ans[-2]+ans[-1])
    if ans[-1] >= max(a,b):
        break
ans1 = []
for i in ans:
    if min(a,b) <= i <= max(a,b):
        ans1.append(str(i))
print(" ".join(ans1))