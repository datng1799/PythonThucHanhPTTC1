Test = int(input())

while (Test != 0):
    Test -= 1
    num_s = str(input());
    max_num = 0
    pos  = 0
    for i in range(0, len(num_s)):
        num_ref = ord(num_s[i]) - ord('0')
        if num_ref>max_num:
            max_num = num_ref
            pos = i
    if pos == 0 or pos == len(num_s)-1:
        print("NO")
        continue
    i1 = pos-1
    i2 = pos+1
    while ((ord(num_s[i1])-ord('0')<ord(num_s[i1+1])-ord('0')) and i1>=0 ):
        i1 -= 1
        if i1 == -1:
            break
    while ((ord(num_s[i2])-ord('0')<ord(num_s[i2-1])-ord('0')) and i2<len(num_s)):
        i2 += 1
        if i2 == len(num_s):
            break
    if (i1 == -1 and i2 == len(num_s)):
        print("YES")
    else:
        print("NO")