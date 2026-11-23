num_s = str(input())

res = ""
str_3 = ""
for i in range(len(num_s)-1, -1, -1):
    if len(str_3)>2:
        res += str_3+ str(',')
        str_3=""
    str_3 += str(num_s[i])
res += str_3
print(res[::-1])