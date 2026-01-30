s = "a"
temp = ""
import string
temp1 = string.punctuation # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# print(temp1)
# temp_list = string.ascii_lowercase+string.ascii_uppercase+string.digits
# for i in s:
#     if i in temp_list:
#         temp += i.lower()
s = s.replace(" ","").lower()
for i in temp1:
    if i in s:
        s = s.replace(i,"")

if s == s[::-1] or s == "":
    print(True)
else:
    print(False)
'''
"A man, a plan, a canal: Panama"
"race a car"
"0P"
" "
"a"
'''