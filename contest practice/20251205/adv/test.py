import sys
input = sys.stdin.readline

MAX = 100000
prime = [True] * (MAX+1)
prime[0] = prime[1] = False

for i in range(2,int(MAX**0.5)+1):
    if prime[i] == True:
        for j in range(i * i,MAX+1,i):
            prime[j] = False


while True:
    st = input()
    if st == '0':
        break
    for i in range(MAX,1,-1):
        if prime[i] and str(i) in st:
            print(i)
            break