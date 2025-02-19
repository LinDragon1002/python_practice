def rank(a):
    temp = [i for i in a.split(',')]
    total = 0
    for i in range(len(temp)):
        total += int(temp[i])
    avg = total / len(temp)
    if avg >= 90:
        return "A"
    elif 75 <= avg < 90:
        return "B"
    elif 60 <= avg < 75:
        return "C"
    else:
        return "D"
    
a = input()
print(rank(a))
        
