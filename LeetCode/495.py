timeSeries = [1,2]
duration = 5
ans = 0

for i in range(len(timeSeries)-1):
    if timeSeries[i]+duration >= timeSeries[i+1]:
        ans += timeSeries[i+1] - timeSeries[i]
    else:
        ans += duration
print(ans+5)

# 另解

total = duration
for i in range(1,len(timeSeries)):
    current_time = timeSeries[i]
    last_time = timeSeries[i-1]
    if current_time<last_time+duration:
        total+= current_time-last_time
    else:
        total+=duration
# return total
print()