def count(num):
    if 1 <= num <= 3:
        return 300 * num
    elif 4 <= num <= 6:
        return count(3) + 250 * (num-3)
    elif 7 <= num <= 12:
        return count(6) + 200 * (num-6)
    else:
        return count(12) + 150 * (num-12)
num = int(input())
print(count(num))