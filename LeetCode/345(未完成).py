s = "IceCreAm"

for i in range(len(s)):
    if s[i].lower() in ("a","e","i","o","u"):
        temp = s[i]
        for j in range(len(s)-1,-1,-1):
            if s[j].lower() in ("a","e","i","o","u"):
                s[i] == s[j]
                s[j] == temp
