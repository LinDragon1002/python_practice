def check(a):
    temp = [i for i in a.split('.')]
    if len(temp) == 4:
        for i in temp:
            if str.isdigit(i) and 1 <= int(i) <= 255:
                ans = True
            else:
                ans = False
                break
        return ans
    else:
        return False
    

a = input()
print(check(a))