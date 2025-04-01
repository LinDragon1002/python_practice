a,b = map(int,input().split())
c = int(input())

for i in range(2,c):
    if i % 2 == 0:
        a = a + b
    else:
        b = a + b
if c % 2 == 0:
    print(b)
else:
    print(a)