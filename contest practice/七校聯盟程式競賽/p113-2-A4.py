people = sorted(input().split(','))
go_out = input().split(',')

ans = [[0,0] for _ in range(len(people))]

for i in range(len(people)):
    if not go_out:
        break
    for j in go_out:
        if j == people[i]:
            ans[i][0] += 1
if go_out != ['']:
    for i in go_out:
        for j in range(len(people)):
            if int(people[j]) > int(i) and int(people[j]) % int(i) == 0:
                ans[j][1] += 1

for i in range(len(ans)):
    print(f"{people[i]}:({ans[i][0]},{ans[i][1]})")