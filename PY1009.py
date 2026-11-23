string_inp = str(input())

lower_count = 0
upper_count = 0

for i in range(0, len(string_inp)):
    acsii_code = ord(string_inp[i])
    if (acsii_code>=97):
        lower_count += 1
    else:
        upper_count += 1

if (lower_count>=upper_count):
    print(string_inp.lower())
else:
    print(string_inp.upper())