from fractions import Fraction
st = input().split(',')
temp = []
operatored = ""
for i in st:
    if i in ("+","-","*","/"):
        operatored += i
    else:
        temp.append(int(i))
num1 = Fraction(temp[0],temp[1])
num2 = Fraction(temp[2],temp[3])
if operatored == "+":
    ans = num1 + num2
elif operatored == "-":
    ans = num1 - num2
elif operatored == "*":
    ans = num1 * num2
elif operatored == "/":
    ans = num1 / num2
print(Fraction(ans))