def counts():
    number = int(input())
    types = ["Spades","Heart","Diamond","Club"]
    numbers = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    if 1 <= number <= 13:
        return f'{types[0]}-{numbers[number-1]}'
    elif 14 <= number <= 26:
        return f'{types[1]}-{numbers[number-14]}'
    elif 27 <= number <= 39:
        return f'{types[2]}-{numbers[number-27]}'
    elif 40 <= number <= 52:
        return f'{types[3]}-{numbers[number-40]}'
print(counts())