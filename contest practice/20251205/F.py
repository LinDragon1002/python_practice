while True:
    try:
        w = int(input())
        n = int(input())
        ans = 0
        for i in range(n):
            a,b = map(int,input().split())
            ans += a * b
        print(int(ans/w))
    except:
        break
