def dfs_post(T):
    stack = []
    opat = ['+','-','*','/']
    for i in T:
        if i in opat:
            right = stack.pop()
            left = stack.pop()
            temp = left + i + right
            stack.append(str(int(eval(temp))))
        else:
            stack.append(i)
    return stack[0]
for _ in range(int(input())):
    T = input().split()
    print(dfs_post(T))