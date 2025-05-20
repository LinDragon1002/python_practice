num = int(input())
ans = ''
temp = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
while num != 0:
    if num > 1000:
        ans += "M" *(num // temp["M"])
        num -= (num // temp["M"]) * 1000
    elif num >500:
        ans += "D" *(num // temp["D"])
        num -= (num // temp["D"]) * 500
    elif num >100:
        ans += "C" *(num // temp["C"])
        num -= (num // temp["C"]) * 100
    elif num >50:
        ans += "L" *(num // temp["L"])
        num -= (num // temp["L"]) * 50
    elif num >10:
        ans += "X" *(num // temp["X"])
        num -= (num // temp["X"]) * 10
    elif num >5:
        ans += "V" *(num // temp["V"])
        num -= (num // temp["V"]) * 5
    elif num > 1:
        ans += "I" *(num // temp["I"])
        num -= (num // temp["I"]) * 1
print(ans)