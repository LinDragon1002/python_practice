digits = [9,9]
for i in range(len(digits)-1,-1,-1):
    if i == len(digits)-1:
        digits[i] += 1
    if digits[i] >= 10:
        digits[i] = 0
        if i-1 == -1:
            digits.insert(0,1)
        else:
            digits[i-1] += 1
print(digits)