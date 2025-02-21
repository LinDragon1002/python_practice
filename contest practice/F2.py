def safe(a):
    temp = 10 - sum([int(i) for i in a]) % 10
    return a + str(temp)

a = input()
print(safe(a))