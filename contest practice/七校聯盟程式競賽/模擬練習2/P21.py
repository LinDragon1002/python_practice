# st= input()
# cnt = 0
# deeps = []
# deeps_types = []
# for i in range(len(st)):
#     if st[i] == "{":
#         cnt += 1
#         deeps.append(cnt)
#         deeps_types.append("{")
#     elif st[i] == "[":
#         cnt += 1
#         deeps.append(cnt)
#         deeps_types.append("[")
#     elif st[i] == "(":
#         cnt += 1
#         deeps.append(cnt)
#         deeps_types.append("(")
#     elif st[i] == "}":
#         cnt -= 1
#         deeps.append(cnt)
#         if cnt != -1 and deeps_types[-1] == "{":
#             deeps_types.pop()
#         else:
#             cnt = -1
#             break
#     elif st[i] == "]":
#         cnt -= 1
#         deeps.append(cnt)
#         if cnt != -1 and deeps_types[-1] == "[":
#             deeps_types.pop()
#         else:
#             cnt = -1
#             break
#     elif st[i] == ")":
#         cnt -= 1
#         deeps.append(cnt)
#         if cnt != -1 and deeps_types[-1] == "(":
#             deeps_types.pop()
#         else:
#             cnt = -1
#             break
# if cnt == 0:
#     print(max(deeps))
# else:
#     print(-1)
st = input()
stack = []
max_depth = 0

# 對應的括號
pairs = {')': '(', ']': '[', '}': '{'}

for ch in st:
    if ch in "({[":
        stack.append(ch)
        max_depth = max(max_depth, len(stack))
    elif ch in ")}]":
        if not stack or stack[-1] != pairs[ch]:
            print(-1)
            break
        stack.pop()
else:
    print(max_depth if not stack else -1)
