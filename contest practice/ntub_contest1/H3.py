def number():
    response = [i for i in input()]
    temp = []
    a = True
    while a:
        ans = 0
        for i in response:
            ans = ans + int(i) ** 2
        for i in temp:
            if ans == i:
                print("False")
                a = False
        temp.append(ans)
        sorted(temp)
        if ans == 1:
            print("True")
            break
        else:
            response = [i for i in str(ans)]
number()