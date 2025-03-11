def service(a,b,services=False):
    if services:
        if a+b >= 4:
            return f'{int(a * 850 + b * 350 + (a * 500 + b * 300) * 0.8):,.0f}元'
        else:
            return f'{a * 1350 + b * 850:,.0f}元'
    else:
        return f'{a * 850 + b * 350:,.0f}元'



print(service(2,4))
print(service(2,2,services=True))
print(service(2,1))
print(service(2,1,services=True))