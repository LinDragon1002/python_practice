def compute_total(item,*quantities):
    if item in ("A","D","E","K"):
        if len(quantities) >= 4:
            return f'{sum(quantities[:3]) * 80 + sum(quantities[3:]) * 80 * 0.8:,.0f}'
        return f'{sum(quantities) * 80:,}'
    elif item in ("B","M","P","R"):
        if len(quantities) >= 4:
            return f'{sum(quantities[:3]) * 60 + sum(quantities[3:]) * 60 * 0.8:,.0f}'
        return f'{sum(quantities) * 60:,}'
    else:
        if len(quantities) >= 4:
            return f'{sum(quantities[:3]) * 50 + sum(quantities[3:]) * 50 * 0.8:,.0f}'
        return f'{sum(quantities) * 50:,}'

print(compute_total("A",15,20,10,40,15))
print(compute_total("P",40,30,20,30,50,60))
print(compute_total("N",20,30))