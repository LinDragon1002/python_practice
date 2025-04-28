num = int(input())
cnt = 1
for i in range(1,num+1):
    print(f'{"-" * (num - i)}{("*" * cnt)}{"-" * (num - i)}')
    cnt += 2
    print()