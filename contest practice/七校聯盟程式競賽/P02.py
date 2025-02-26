def mountain():
    response = input()
    temp = sorted(response, reverse=True)
    if response.count(temp[0]) == 1 and temp[0] != response[0] and temp[0] != response[-1]:
        return 1
    return 0
print(mountain())