n = int(input())
if n <= 2500 :
    temp1 = 1
    if n % 25 == 0:
        temp2 = n // 25
        temp3 = 25
    else:
        temp2 = n // 25 + 1
        temp3 = n % 25
elif 2500 < n <= 7500:
    temp1 = 2
    n = n - 2500
    if n % 50 == 0:
        temp2 = n // 50
        temp3 = 50
    else:
        temp2 = n // 50 + 1
        temp3 = n % 50
else:
    temp1 = 3
    n = n - 7500
    if n % 25 == 0:
        temp2 = n // 25
        temp3 = 25
    else:
        temp2 = n // 25 + 1
        temp3 = n % 25
print(f"{temp1} {temp2} {temp3}")