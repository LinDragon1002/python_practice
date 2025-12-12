import sys
input = sys.stdin.readline

n, q = map(int,input().split())
n_list = list(map(int,input().split()))

prefix = [0] * (n+1)
prefix[1] = n_list[0]
for i in range(2,n+1):
    prefix[i] = prefix[i-1] + n_list[i-1]

for i in range(q):
    a,b = map(int,input().split())
    print(prefix[b] - prefix[a-1])