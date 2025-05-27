# Queue, 佇列
'''
|---------------------------------|
|              Queue              |
|---------------------------------|
| - data: list                    |
|---------------------------------|
| + 建構元()                      |
| + enqueue(int):none             |
| + degueue():int                 |
| + size():int                    |
|---------------------------------|
'''
class Queue:
    # 建構元
    def __init__(self):
        self.__data = []
    # 加入資料
    def enqueue(self, item):
        self.__data.append(item)
    # 移除資料
    def dequeue(self):
        return self.__data.pop(0) if self.size() > 0 else None
    # 取得佇列大小
    def size(self):
        return len(self.__data)
    # 印出物件時自動呼叫
    def __str__(self):
        return f'首{self.__data}尾'

# 測試
# q1 = Queue()
# q1.enqueue(10)
# q1.enqueue(20)
# q1.enqueue(30)
# print(q1.size())
# print(q1)
# q1.dequeue()
# print(q1.size())
# print(q1)
# q1.dequeue()
# print(q1.size())
# print(q1)
# q1.dequeue()
# print(q1.size())
# print(q1)
# q1.dequeue()
# print(q1.size())
# print(q1)

# Stack, 堆疊
'''
|---------------------------------|
|              Stack              |
|---------------------------------|
| - data: list                    |
|---------------------------------|
| + 建構元()                      |
| + push(int):none                |
| + pop():int                     |
| + size():int                    |
|---------------------------------|
'''

class Stack():
    # 建構元
    def __init__(self):
        self.__data = []
    # 加入資料
    def push(self, item):
        self.__data.append(item)
    # 移除資料
    def pop(self):
        return self.__data.pop() if self.size() > 0 else None
    # 取得堆疊大小
    def size(self):
        return len(self.__data)
    # 印出物件時自動呼叫
    def __str__(self):
        return f'頂{self.__data}底'

# 測試
# q1 = Stack()
# q1.push(10)
# q1.push(20)
# q1.push(30)
# print(q1.size())
# print(q1)
# q1.pop()
# print(q1.size())
# print(q1)
# q1.pop()
# print(q1.size())
# print(q1)
# q1.pop()
# print(q1.size())
# print(q1)
# q1.pop()
# print(q1.size())
# print(q1)

# Node, 節點
'''
|---------------------------------|
|              Node               |
|---------------------------------|
|<<get/set>> - data: int          |
|<<get/set>> - next: Node         |
|---------------------------------|
| + 建構元()                      |
|---------------------------------|
'''

class Node:
    # 建構元
    def __init__(self, data=None):
        self.__data = data
        self.next = None

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, next):
        self.__next = next

# 測試
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
# 刪除節點q
# p = head
# q = p.next
# p.next = q.next
# while p:
#     print(p.data)
#     p = p.next

# 在10,20之間增加50
p = head
q = p.next
k = Node(50)
k.next = q
p.next = k

while p:
    print(p.data)
    p = p.next
