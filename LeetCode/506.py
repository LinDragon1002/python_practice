score = [10,3,8,9,4]
temp_score = score.copy()
temp_score = sorted(temp_score,reverse=True)
ranks = ["Gold Medal","Silver Medal","Bronze Medal"]
ans = ["0"] * len(score)
for i in range(len(temp_score)):
    find_th = score.index(temp_score[i])
    if i < 3:
        ans[find_th] = ranks[i]
    else:
        ans[find_th] = str(i+1)
print(ans)


# 另解

sorted_scores = sorted(score, reverse=True)
        
'''
rank_map = {}

for i, val in enumerate(sorted_scores):
    if i == 0:
        rank_map[val] = "Gold Medal"
    elif i == 1:
        rank_map[val] = "Silver Medal"
    elif i == 2:
        rank_map[val] = "Bronze Medal"
    else:
        rank_map[val] = str(i + 1)

return [rank_map[s] for s in score]
'''