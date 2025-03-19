from itertools import permutations
def counts():
    st = input()
    temp = []
    for i in permutations(st):
        temp.append(int(''.join(i)))
    temp = list(set(temp))
    temp.remove(int(st))
    temp = sorted(temp,reverse=True)
    for i in temp:
        print(i) 
counts()