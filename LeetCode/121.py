prices = [7,6,4,3,1]
ans = 0
min_price = prices[0]
extends = 0

for i in range(1,len(prices)):
    if prices[i] < min_price:
        min_price = prices[i]
    else:
        extends = max(extends, prices[i]-min_price)
print(extends)





'''
[7,1,5,3,6,4]
[7,6,4,3,1]
'''