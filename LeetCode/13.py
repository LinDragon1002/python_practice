s = "MCMXCIV"
temp = {"I": 1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
ans = 0
prev = 0
for i in reversed(s):
    val = temp[i]
    if val < prev:
        ans -= val
    else:
        ans += val
        prev = val
print(ans)