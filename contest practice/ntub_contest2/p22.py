def Hamming():
    a,b = format(int(input()),"b"),format(int(input()),"b")
    if len(a) < len(b):
        a = (len(b) - len(a)) * "0" + a
    elif len(b) < len(a):
        b = (len(a) - len(b)) * "0" + b
    ans3 = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            ans3 += 1
    print(ans3)
Hamming()