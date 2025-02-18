#a004

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

running =True
while True:
    try:
        year = input()
        year = int(year)
        if year % 4 == 0  and year % 100 != 0:
            print('閏年')
        elif year % 400 == 0:
            print('閏年')
        else:
            print('平年')
    except:
        break