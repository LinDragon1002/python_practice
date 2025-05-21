num = input()
max_num = sorted(num,reverse=True)
min_num = sorted(num)
print(int("".join(max_num)) - int("".join(min_num)))