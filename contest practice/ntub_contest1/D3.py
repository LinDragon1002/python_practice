def evaluation(a):
    a = [i for i in a.split(',')]
    total = 0
    temp = {"A+":95,"A":90,"A-":85,"B+":80,"B":75,"B-":70,"C+":65,"C":60,"C-":50}
    for i in range(len(a)):
        if a[i] in temp:
            total += temp[a[i]]
    if total//len(a) >= 90:
        return "A"
    elif total//len(a) >= 80:
        return "B"
    elif total//len(a) >= 70:
        return "C"
    elif total//len(a) >= 60:
        return "D"
    else:
        return "E"
    
a = input()
print(evaluation(a))
