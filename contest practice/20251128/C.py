st = input().split()

stack = []
opat = ['+','-','*','/','(',')']
ans = []
def priority(op):
    if op in ['+', '-']:
        return 1
    elif op in ['*', '/']:
        return 2
    return 0
for i in st:
    if i in opat:
        if stack == [] or i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                ans.append(stack.pop())
            if stack:
                stack.pop()
        else:
            while stack and stack[-1] != '(' and priority(stack[-1]) >= priority(i):
                ans.append(stack.pop())
            stack.append(i)
    else:
        ans.append(i)

while stack:
    ans.append(stack.pop())
print(*ans)
