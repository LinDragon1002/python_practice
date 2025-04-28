num1 = int(input())
st = input()
num2 = int(input())

if st in ("+", "-", "*", "/"):
    if st == "/" and num2 == 0:
        print("error")
    elif st == "/":
        ans = eval(f"{num1}{st}{num2}")
        print(f'{num1}{st}{num2}={ans:.2f}')
    else:
        ans = eval(f"{num1}{st}{num2}")
        print(f"{num1}{st}{num2}={ans}")
else:
    print("error")