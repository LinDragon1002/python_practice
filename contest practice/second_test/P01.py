a,b,c,d = map(int,input().split())
if b-a == c-b == d-c:
    print(f'A\n{b-a}')
elif b//a == c//b == d//c:
    print(f'G\n{b//a}')
