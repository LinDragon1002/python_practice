def check(a):
    temp = [0,0]
    for i in a:
        if i == "(":
            temp[0] += 1
        elif i == ")":
            temp[1] += 1
        if temp[0] < temp[1]:
            return False
    if temp[0] == temp[1]:
        return True
    else:
        return False

a = input()
print(check(a))