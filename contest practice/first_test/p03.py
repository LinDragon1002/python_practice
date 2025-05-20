# def numbers():
#     number = input()
#     temp2 = []
#     # for i in range(len(number)):
#     #     ans[0] += int(number[i])
#     first_sum = [int(i) for i in number]

#     # for i in range(2,int(number)):
#     #     if int(number)%i == 0:
#     #         temp2.append(i)
#     # if len(temp2) == 0:
#     #     return 0
#     # else:
#     #     number1 = []
#     #     for i in temp2:
#     #         while int(number)%i == 0:
#     #             if int(number)%i == 0:
#     #                 number1.append(i)
#     #                 number = int(number)//i
#     number = int(number)
#     for i in range(2,number):
#         while number % i == 0:
#             temp2.append(i)
#             number //= i
#     if not temp2:
#         return 0

#     factors = 0
#     for i in range(len(temp2)):
#         temp3 = [int(i) for i in str(temp2[i])]
#         # for j in range(len(temp3)):
#         #     ans[1] += temp3[j]
#         factors += sum(temp3)

#     if first_sum[0] == factors:
#         return 1
#     return 0
# print(numbers())
def find_prime_factors(n):
    temp = n
    factors = set()
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 1
    if n > 1:
        factors.add(n)
    if temp in factors:
        factors.remove(temp)
    return sorted(factors)
num = int(input())
temp = find_prime_factors(num)
temp.append(num)
ans = []
for i in range(len(temp)):
    op = [int(i) for i in str(temp[i])]
    ans.append(sum(op))
if ans[-1] == sum(ans) - ans[-1]:
    print(1)
else:
    print(0)