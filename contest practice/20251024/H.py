def f91(n):
    if n <= 100:
        return f91(f91(n + 11))
    else:
        return n - 10
n = []
ans = []
while True:
    a = int(input())
    if a == 0:
        break
    else:
        n.append(a)
        ans.append(f91(a))
for i in range(len(n)):
    print(f"f91({n[i]}) = {ans[i]}")