import sys
sys.setrecursionlimit(1000000)
from collections import defaultdict
def dfs(Tree, now_node):
    count = 0
    # print(now_node, end=" ")
    for next_node in Tree[now_node]:
        count += dfs(Tree,next_node)
        count += 1
    counts[now_node-1] = count
    return count

tree = defaultdict(list)
num = int(input())
top_number = input().split(' ')
temp = {}
counts = [0] * num
temp_no = 0
root = 1
for i in range(2,len(top_number)+2):
    temp[i] = int(top_number[temp_no])
    temp_no+=1
for i in range(1,num+1):
    temp_list = []
    for key in temp:
        if temp[key] == i:
            temp_list.append(key)
    tree[i].extend(temp_list)

dfs(tree,root)
# for i in range(1,num+1):
#     print(tree[i])
print(*counts)