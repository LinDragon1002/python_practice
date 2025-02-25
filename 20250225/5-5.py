
def service(a,b,services=False,express=False):
    if services and express:
        return f'{a * 2150 + b * 700 + b // 2 * 420 + b % 2 * 300:,.0f}元'
    elif services:
        return f'{a * 1350 + b *350 + b // 2 * 420 + b % 2 * 300:,.0f}元'
    elif express:
        return f'{a * 1650 + b * 700:,.0f}元'
    else:
        return f'{a * 850 + b * 350:,.0f}元'



print(service(2,3))
print(service(2,3,services=True))
print(service(2,3,express=True))
print(service(2,3,services=True,express=True))