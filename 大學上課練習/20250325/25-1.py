def compute_total(degree):
    if degree <= 330:
        return 3.02*degree
    elif degree <= 700:
        return 5.44 * (degree-330) + compute_total(330)
    elif degree <= 1000:
        return 6.16 * (degree-700) + compute_total(700)
    else:
        return (degree-1000) * 6.71 + compute_total(1000)
print(compute_total(1250))