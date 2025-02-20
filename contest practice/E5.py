def Hamming(a,b):
    '''
    a,b = str(bin(int(a))).replace("0b",""),str(bin(int(b))).replace("0b","")
    if len(a) < 20:
        a = (20 - len(a)) * "0" + a
    if len(b) < 20:
        b = (20 - len(b)) * "0" + b
    '''
    a,b = format(a,"020b"),format(b,"020b")
    
    print(f'{a}\n{b}')
    ans3 = 0
    for i in range(20):
        if a[i] != b[i]:
            ans3 += 1
    print(ans3)

a,b = map(int,input().split(' '))
Hamming(a,b)