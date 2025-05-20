num = int(input())
cnt = 0
st = input()
for i in range(len(st)):
    if st[i].isdigit():
        cnt += 1
if num == cnt:
    print(1)
else:
    print(0)