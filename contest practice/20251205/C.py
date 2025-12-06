while True:
    try:
        temp = list(map(int,input().split()))
        print(2 * temp[0] * temp[1])
    except:
        break