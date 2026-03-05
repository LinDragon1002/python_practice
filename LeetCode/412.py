n = 3
ans = []

for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        ans.append("FizzBuzz")
    elif i % 5 == 0:
        ans.append("Buzz")
    elif i % 3 == 0:
        ans.append("Fizz")
    else:
        ans.append(f"{i}")
print(ans)