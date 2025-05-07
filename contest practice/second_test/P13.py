from math import gcd,lcm

up1,down1 = list(map(int,input().split(',')))
up2,down2 = list(map(int,input().split(',')))

lcm_down = lcm(down1,down2)
if down1 != lcm_down or down2 != lcm_down:
    if down2 != lcm_down:
        up2 *= (lcm_down // down2)

    up1  *= (lcm_down // down1)
    up = up1 + up2
    ans = gcd(up,lcm_down)

    if ans != 1:
        up //= ans
        lcm_down //= ans
else:
    up = up1 + up2
    ans = gcd(up,lcm_down)
    if ans != 1:
        up //= ans
        lcm_down //= ans

print(f"{up}/{lcm_down}")
