# -*- coding: utf-8 -*-
"""1008.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FGPJdn979FK3Mhgz83OaYoyM5LHfWwOQ
"""

number = input()
amount = int(input())
price = 0

if number == "A":
  price = 10.5
else:
  price = 15.7

total = price * amount

print(f'總金額:{total:,.0f}元')

import math
number = input()
amount = int(input())
price = 0

if number == "A":
  price = 10.5
else:
  price = 15.7

total = math.ceil(price * amount)

print(f'總金額:{total:,.0f}元')

import math
number = input()
amount = int(input())
price = 0

if number == "A" or number == "B" or number == "E":
  price = 10.5
else:
  price = 15.7

total = math.floor(price * amount)

print(f'總金額:{total:,.0f}元')

import math
number = input()
amount = int(input())
price = 0

if number in ('A','B','E'):
  price = 10.5
else:
  price = 15.7

total = math.floor(price * amount)

print(f'總金額:{total:,.0f}元')

#不推薦 因為AB、AE、BE、ABE也會在其中
import math
number = input()
amount = int(input())
price = 0

if number in 'ABE':
  price = 10.5
else:
  price = 15.7

total = math.floor(price * amount)

print(f'總金額:{total:,.0f}元')

#tuple 不能更改
a = ('A','B','E')
print(id(a))
print(a[0])
print(a[1])

a = ('A','B','E','F')
print(id(a))
for i in a:
  print(i)

a = ['A','B','E']
print(id(a))
print(a[0])
print(a[1])
a.append('C')
print(id(a))
for i in a:
  print(i)

#str is 不可更改需重新建立新str
a = "ABE"
print(type(a))

for i in a:
  print(i)

import math
number = input()
amount = int(input())
price = 0

if number[0:2] == "AB":
  price = 10.5
else:
  price = 15.7

total = math.floor(price * amount)

print(f'總金額:{total:,.0f}元')

import math
number = input()
amount = int(input())
price = 0

if number[-2:] == "12":
  price = 10.5
else:
  price = 15.7

total = math.floor(price * amount)

print(f'總金額:{total:,.0f}元')

import math
number = input()
amount = int(input())
price = 0

if number == "A":
  price = 10.5
else:
  if number == "B":
    price = 15.7
  else:
    if number == "C":
      price = 16.9
    else:
      price = 20.3

total = math.floor(price * amount)

print(f'總金額:{total:,.0f}元')

import math
number = input()
amount = int(input())
price = 0

if number == "A":
  price = 10.5
elif number == "B":
  price = 15.7
elif number == "C":
  price = 16.9
else:
  price = 20.3

total = math.floor(price * amount)

print(f'總金額:{total:,.0f}元')

number = input()
amount = int(input())
price = 0

if number == "A":
  if amount >= 100:
    price = 10.5
  else:
    price = 12.3
else:
  price = 15.7

total = int(price * amount)

print(f'總金額:{total}')

area = input()
price = int(input())
amount = int(input())

total = price * amount

if area in ('A','D','E'):
  total1 = total * 0.8
elif area in ('B','C','F'):
  total1 = total * 0.9
elif area in ('G','I','K'):
  total1 = total * 0.95
else:
  total1 = total

print(f'折扣前金額={total:,.0f}, 折扣後金額={total1:,.0f}元')

area = input()
price = int(input())
amount = int(input())

total = price * amount

if area in ('A','D','E'):
  total1 = total * 0.7
elif area in ('B','C','F'):
  total1 = total * 0.8
elif area in ('G','I','K'):
  total1 = total * 0.9
else:
  total1 = total * 0.95

print(f'折扣前金額={total:,.0f}, 折扣後金額={total1:,.0f}元')

area = input()
amount = int(input())

if area == "A":
  total = 200 * amount
  if total >= 2000:
    total1 = total * 0.85
  else:
    total1 = total * 0.95
elif area == "B":
  total = 100 * amount
  total1 = total * 0.9
else:
  total = 50 * amount
  total1 = total

print(f'折扣前金額={total:,.0f}元, 折扣後金額={total1:,.0f}元')