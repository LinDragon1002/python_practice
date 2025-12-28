def postfix(expression):
    stack = []
    for tocken in expression:
        if tocken.isdigit():
            stack.append(int(tocken))
        else:
            b = stack.pop()
            a = stack.pop()
            if tocken == '+':
                stack.append(a + b)
            elif tocken == '-':
                stack.append(a - b)
            elif tocken == '*':
                stack.append(a * b)
            elif tocken == '/':
                stack.append(int(a / b))
    return stack[0]

num = int(input())

for i in range(num):
    st = input().split()
    print(postfix(st))