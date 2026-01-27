s = "}"
temp = {"}":"{",")":"(","]":"["}

stack = []

for i in s:
    if i in temp:
        if len(stack) > 0 and temp[i] == stack[-1]:
            stack.pop()
        else:
            print(False)
    else:
        stack.append(i)
if len(stack) > 0:
    print(False)
else:
    print(True)