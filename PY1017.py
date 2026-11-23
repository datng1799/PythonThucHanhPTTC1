import math as mth
Test = int(input())

while (Test != 0):
    Test -= 1
    num_s = str(input().strip())
    if (len(num_s)<2):
        print("NO")
        continue
    ok = True
    element_1 = ord(num_s[0]) - ord('0')
    sum = element_1
    for i in range(1, len(num_s)):
        element_2 = ord(num_s[i]) - ord('0')
        if mth.fabs(element_1-element_2)!=2:
            ok = False
            break
        sum += element_2
        element_1 = element_2
    if (ok and sum%10 == 0):
        print("YES")
    else:
        print("NO")