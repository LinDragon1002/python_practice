moves = "RRDD"
ans = [0,0]

temp = {"U":1,"R":1,"D":-1,"L":-1}

for i in moves:
    if i in ("U","D"):
        ans[1] += temp[i]
    else:
        ans[0] += temp[i]
if ans.count(0) == 2:
    print(True)
else:
    print(False)

# 另解
# return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")