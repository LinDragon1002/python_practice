def is_valid_parentheses(st):
    stack = []
    mapping = {'}' : '{' , ']' : '[' , ')' : '('}
    
    for i in st:
        if i in mapping.values():
            stack.append(i)
        elif i in mapping:
            if not stack or stack.pop() != mapping[i]:
                return False
    return len(stack) == 0

num = int(input())

for i in range(num):
    st = input()
    if is_valid_parentheses(st):
        print("Yes")
    else:
        print("No")