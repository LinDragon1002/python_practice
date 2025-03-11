def compute_total(**items):
    total = 0
    for key in items:
        if key in ("A","B","D"):
            total += items[key] *150
        else:
            total += items[key] *100
    return f'總金額 = {total}元'
print(compute_total(A=3,B=2))
print(compute_total(C=1,D=2))
print(compute_total(M=1,P=2))