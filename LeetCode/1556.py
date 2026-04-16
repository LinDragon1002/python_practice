n = 2251693
ans = ''
for i in range(len(str(n)) // 3):
    if len(str(n)) > 3:
        temp =  '.' + str(n % 1000).zfill(3)
        ans = temp + ans
        n //= 1000
print(str(n)+ans)

# 另解

"""
return f"{n:,}".replace(",", ".")
"""