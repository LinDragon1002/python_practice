num = 14
counts = 0
while num > 0:
    if num % 2 == 0:
        num /= 2
    else:
        num -= 1
    counts += 1
print(counts)