def number():
    answer = int(input())
    ans = 1
    if answer == 1 or answer == 0:
        print("False")
        return
    for i in range(2,answer):
        if answer%i == 0:
            ans += i
    if ans == answer:
        print("True")
    else:
        print("False")
number()