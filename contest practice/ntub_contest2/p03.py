def number():
    response = [int(i) for i in input()]
    temp = 1
    temp1 = 0
    for i in range(len(response)):
        temp *= response[i]
        temp1 += response[i]
    return temp - temp1
print(number())