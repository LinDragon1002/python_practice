def infix_to_postfix(expression):
    op = {'+': 1,'-':1,'*':2,'/':2}
    stack = []
    output = []

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while(stack and stack[-1] != '(' and op.get(stack[-1],0) >= op.get(char,0)):
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())

    return " ".join(output)

st = input().split()
print(infix_to_postfix(st))