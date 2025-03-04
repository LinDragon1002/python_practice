def compute_total(item,*quantities):
    if len(quantities) == 0:
        return 0
    if item == "A":
        return f'{sum(quantities) * 80:,}'
    return f'{sum(quantities) * 50:,}'

print(compute_total("A",15,20,10))
print(compute_total("B",40))
print(compute_total("C"))
