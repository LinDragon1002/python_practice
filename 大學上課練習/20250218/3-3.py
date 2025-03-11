def weighted_avg(chi,eng):
    if chi > eng:
        return round((chi*2 + eng*1.5) / 3.5,2)
    else:
        return round((eng*2 + chi*1.5) / 3.5,2)

chi = 55
eng = 60
print(weighted_avg(chi,eng))