n = 5
ans = [] 
for i in range(n+1):
    ans.append(str(bin(i)).count("1"))
print(ans)

print([x.bit_count() for x in range(n+1)])