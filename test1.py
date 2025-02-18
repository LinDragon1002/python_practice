# # a003
# a,b = map(int,input().split())
# M = a
# D = b

# S = (M*2+D)%3
# if S == 0:
#     print("普通")
# elif S == 1:
#     print("吉")
# elif S == 2:
#     print("大吉")

# # a004

# try:
#     running = True
#     while running:
#         year = input()
#         if year == '':
#             break
#         year = int(year)
#         if year % 4 == 0  and year % 100 != 0:
#             print('閏年')
#         elif year % 400 == 0:
#             print('閏年')
#         else:
#             print('平年')
# except EOFError:
#     running =True
#     while running:
#         year = input()
#         if year == '':
#             break
#         year = int(year)
#         if year % 4 == 0  and year % 100 != 0:
#             print('閏年')
#         elif year % 400 == 0:
#             print('閏年')
#         else:
#             print('平年')

# running =True
# while True:
#     try:
#         year = input()
#         year = int(year)
#         if year % 4 == 0  and year % 100 != 0:
#             print('閏年')
#         elif year % 400 == 0:
#             print('閏年')
#         else:
#             print('平年')
#     except:
#         break

# # a005
# a = int(input())
# for i in range(0,a):
#     a1,a2,a3,a4 = map(int,input().split())
#     if int(a2 / a1) == int(a4 / a3):
#         r = a2 /a1 
#         arrange = []
#         arrange.append(a1)
#         for e in range(4):
#             arrange.append(a1*int(r))
#             a1 *= int(r)
#         print(*arrange, sep=" ")
#         arrange.clear()
#     elif a2 - a1 == a4 - a3:
#         d = a2 - a1
#         arrange1 = []
#         arrange1.append(a1)
#         for e in range(4):
#             arrange1.append(a1+d)
#             a1 += d
#         print(*arrange1, sep=" ")
#         arrange1.clear()
    

# # a006

# a,b,c = map(int,input().split())
# x1 =(-b + (b**2-4*a*c)**0.5)/(2*a)
# x2 =(-b - (b**2-4*a*c)**0.5)/(2*a)
# if b**2-4*a*c > 0:
#     print(f'Two different roots x1={x1:.0f} , x2={x2:.0f}')
# elif b**2-4*a*c == 0:
#     print(f'Two same roots x={x2:.0f}')
# else:
#     print('No real root')

# # a009

# a = input()
# for i in a:
#     print(chr(ord(i)-7),end='')

# # a010(因數分解)
# answer = int(input())
# number = []
# for i in range(2,answer):
#     if answer%i == 0:
#         number.append(i)
# if len(number) == 0:
#     print(answer)
# else:
#     count = 0
#     number1 = []
#     for i in number:
#         count = 0
#         while answer%i == 0:
#             if answer%i == 0:
#                 count += 1
#                 answer = answer//i
#         if count > 1:
#             number1.append(f'{i}^{count}')
#         elif count == 1:
#             number1.append(i)
#     print(*number1,sep=' * ')
        
# answer = int(input())
# number = []
# for i in range(2,answer):
#     count = 0
#     while answer%i == 0:
#         count += 1
#         answer = answer//i
#     if count > 1:
#         number.append(f'{i}^{count}')
#     elif count == 1:
#         number.append(i)
#     while answer <= 1:
#         break
# if len(number) == 0:
#     print(answer)
# else:
#     print(*number,sep=' * ')

# answer = int(input())
# i = 2
# s = ''
# while answer > 1:
#     count = 0
#     while answer%i == 0:
#         count += 1
#         answer = answer//i
#     if count > 1:
#         s += str(i)+'^'+str(count)
#     if count == 1:
#         s += str(i)
#     if answer%(i+1) == 0 and s != '':
#         s += ' * '
#     i += 1
# print(s)

# answer = int(input())
# number = []
# for i in range(2,answer+1):
#     if answer == 1:
#         break
#     count = 0
#     while answer%i == 0:
#         count += 1
#         answer = answer//i
#     if count > 1:
#         number.append(f'{i}^{count}')
#     elif count == 1:
#         number.append(i)  
# print(*number,sep=' * ')

# while True:

#     try:
#         _input = int(input())
#         factorsCount = 0
#         factor = 2
#         s = ''
#         while _input > 1:
#             while _input % factor == 0:
#                 _input = _input // factor
#                 factorsCount += 1
#             if factorsCount > 1:
#                 s += str(factor) + '^' + str(factorsCount)
#             if factorsCount == 1:
#                 s += str(factor)
#             if _input % (factor + 1) == 0 and s != '':
#                 s += ' * '
#             factorsCount = 0
#             factor += 1
#         print(s)
#     except:
#         break

# # a013
# number = ['I','V','X','L','C','D','M']
# while True:
#     a = map(str,input().split())

# # 阿姆斯壯數
# a,b = map(int,input().split())
# d = 0
# e = 0
# for i in range(a,b+1):
#     for j in str(i):
#         d = d + int(j)**len(str(i))
#     if d == i:
#         print(i,end=" ")
#         e += 1
#     d = 0
# if e == 0:
#     print("none")

# a = int(input())
# b = int(input())
# e = 0
# count = 0
# answer = []
# for i in range(a,b+1):
#     c = len(str(i))
#     d = [e for e in str(i)]
#     for g in d:
#         count = count + int(g)**c
#     if i == count:
#         answer.append(count)
#         e += 1
#         count = 0
#     else:
#         count = 0
#         continue
# if e == 0:
#     print("none")
# else:
#     for g in answer:
#         print(g,end=" ")

# while True:
#     try:
#         a = int(input())
#         a = a**2-a+2
#         print(a)
#     except:
#         break

# while True:

#     try:
#         a = int(input())
#         a = (a ** 3 + 5*a +6)//6
#         print(a)
#     except:
#         break