def sentense():
    response = [i for i in input().split(" ")]
    number = int(input())
    ans = ""
    for i in range(number):
        if i < number - 1:
            ans += response[i] + " "
        else:
            ans += response[i]
    return ans
print(sentense())