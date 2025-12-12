MAX = 100000
Prime = [True] * (MAX+1)
Prime[0] = Prime[1] = False

for i in range(2,int(MAX**0.5)+1):
    if Prime[i]:
        for j in range(i * i,MAX+1, i):
            Prime[j] = False

while True:
    st = input()
    if st == '0':
        break
    for k in range(MAX,1,-1):
        if Prime[k] and str(k) in st:
            print(k)
            break