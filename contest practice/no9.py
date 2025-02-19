def department(a):
    a = a[:2]
    name = {'IS':'資訊部','AC':'會計部','HR':'人資部','MA': '管理部','TR': '運輸部','FA': '製造部'}
    for key in name:
        if key == a:
            return name[key]
    return "錯誤"
a = input()
print(department(a))