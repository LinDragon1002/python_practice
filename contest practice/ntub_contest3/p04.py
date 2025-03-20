from itertools import permutations
def permutation():
    st = input()
    temp = []
    for i in permutations(st):
        temp.append(int(''.join(i)))
    temp.remove(int(st))
    ans = sorted(set(temp),reverse=True)
    for i in ans:
        print(i)
permutation()