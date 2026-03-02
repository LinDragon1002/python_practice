s = 'bd'

'''在 Python 中，若要對列表進行去重（類似 set）但又要保持原始順序，
最有效率的方法是使用 dict.fromkeys()，例如 list(dict.fromkeys(data))。
這利用了 Python 3.7+ 字典保持鍵插入順序的特性，比 set 更高效且能排序。 
'''

for i in list(dict.fromkeys(s)):
    if s.count(i) == 1:
        print(s.index(i))
        break
else:
    print(-1)
