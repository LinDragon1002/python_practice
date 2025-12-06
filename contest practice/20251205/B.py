n = int(input())
list_temp = {"Tetrahedron":4,"Cube":6,"Octahedron":8,"Dodecahedron":12,"Icosahedron":20}
ans = 0
for _ in range(n):
    str_temp = input()
    if str_temp in list_temp:
        ans += list_temp[str_temp]
print(ans)