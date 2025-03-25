def factorial(n):
    r = 1
    for i in range(1,n+1):
        r*=i
    return r

def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial2(n-1)
# print(factorial2(10))

def factorial3(n,mydict={}):
    if n == 1:
        return 1
    elif n in mydict:
        return mydict[n]
    else:
        k = n * factorial3(n-1)
        mydict[n] = k
        return k

def powerof(x,n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / powerof(x,-n)
    else:
        return x * powerof(x,n-1)
# print(powerof(2,20))

def fibonacc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacc(n-1) + fibonacc(n-2)
print(fibonacc(20))

from itertools import permutations
def mypermutations(data):
    myset = set()
    for d in permutations(data):
        myset.add(d)
    return len(myset)
print(mypermutations([1,2,3]))

# 加入集合
myset = set()
# myset.add([1,2,3]) # 不能雜湊 unhashable
print(hash((1,2,3)))
print(hash((1,2,4)))
print(hash(1))
print(hash("1"))